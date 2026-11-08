#!/usr/bin/env python3
"""Format Meetily transcripts for meeting-minute generation.

Usage:
    python3 load_transcript.py <recording directory or transcripts.json>
    python3 load_transcript.py --list
    python3 load_transcript.py --latest
"""
import glob
import json
import os
import sys

RECORDINGS_DIR = os.path.expanduser("~/Movies/meetily-recordings")


def recordings():
    result = [item for item in glob.glob(os.path.join(RECORDINGS_DIR, "*")) if os.path.isdir(item)]
    return sorted(result, reverse=True)


def resolve(path):
    if os.path.isdir(path):
        transcript = os.path.join(path, "transcripts.json")
        if os.path.exists(transcript):
            return transcript, os.path.join(path, "metadata.json")
        raise SystemExit(f"transcripts.json が見つかりません: {path}")
    if os.path.isfile(path):
        return path, os.path.join(os.path.dirname(path), "metadata.json")
    raise SystemExit(f"パスが存在しません: {path}")


def duration(seconds):
    if seconds is None:
        return "不明"
    hours, remainder = divmod(int(seconds), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}時間{minutes}分{seconds}秒" if hours else f"{minutes}分{seconds}秒"


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        raise SystemExit(1)
    if args[0] == "--list":
        for item in recordings():
            print(os.path.basename(item))
        return
    target = recordings()[0] if args[0] == "--latest" and recordings() else args[0]
    if args[0] == "--latest" and not recordings():
        raise SystemExit(f"録音が見つかりません: {RECORDINGS_DIR}")
    transcript_path, metadata_path = resolve(target)
    metadata = json.load(open(metadata_path)) if os.path.exists(metadata_path) else {}
    data = json.load(open(transcript_path))
    segments = data.get("segments", [])
    print("会議メタデータ")
    print(f"会議名     : {metadata.get('meeting_name', '不明')}")
    print(f"開始        : {metadata.get('created_at', '不明')}")
    print(f"終了        : {metadata.get('completed_at', '不明')}")
    print(f"録音時間    : {duration(metadata.get('duration_seconds'))}")
    print(f"言語        : {metadata.get('detected_summary_language', '不明')}")
    print(f"セグメント数: {len(segments)}\n\n発話ログ (display_time | confidence | text)")
    for segment in segments:
        body = segment.get("text", "").strip()
        if body:
            uncertain = " [?]" if isinstance(segment.get("confidence"), (int, float)) and segment["confidence"] < 0.4 else ""
            print(f"{segment.get('display_time', '??:??:??')}{uncertain} {body}")


if __name__ == "__main__":
    main()
