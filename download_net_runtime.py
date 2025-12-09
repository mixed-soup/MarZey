#!/usr/bin/env python3

import os
import sys
import urllib.request
import tarfile
import zipfile
import shutil
from typing import List, Optional

PLATFORM_WINDOWS = "windows"
PLATFORM_LINUX = "linux"
PLATFORM_MACOS = "mac"

DOTNET_RUNTIME_VERSION = "10.0.0"

DOTNET_RUNTIME_DOWNLOADS = {
    PLATFORM_LINUX: "https://builds.dotnet.microsoft.com/dotnet/Runtime/10.0.0/dotnet-runtime-10.0.0-linux-x64.tar.gz",
    PLATFORM_WINDOWS: "https://builds.dotnet.microsoft.com/dotnet/Runtime/10.0.0/dotnet-runtime-10.0.0-win-x64.zip",
    PLATFORM_MACOS: "https://builds.dotnet.microsoft.com/dotnet/Runtime/10.0.0/dotnet-runtime-10.0.0-osx-x64.tar.gz"
}

p = os.path.join


def main() -> None:
    print("="*60)
    print("download_net_runtime.py started")
    print(f"Arguments: {sys.argv}")
    print("="*60)
    update_netcore_runtime(sys.argv[1:])


def update_netcore_runtime(platforms: List[str]) -> None:
    print(f"Starting runtime download for platforms: {platforms}")
    runtime_cache = p("Dependencies/dotnet")
    version_file_path = p(runtime_cache, "VERSION")

    print(f"Runtime cache directory: {runtime_cache}")

    # Check if current version is fine.
    current_version: Optional[str]

    try:
        with open(version_file_path, "r") as f:
            current_version = f.read().strip()

    except FileNotFoundError:
        current_version = None

    print(f"Current cached version: {current_version}")
    print(f"Expected version: {DOTNET_RUNTIME_VERSION}")

    if current_version != DOTNET_RUNTIME_VERSION and os.path.exists(runtime_cache):
        print("Clearing outdated cache...")
        shutil.rmtree(runtime_cache)

    print(f"Creating/ensuring {runtime_cache} directory exists")
    os.makedirs(runtime_cache, exist_ok=True)

    print(f"Writing version file: {version_file_path}")
    with open(version_file_path, "w") as f:
        f.write(DOTNET_RUNTIME_VERSION)

    # Download missing runtimes if necessary.
    if not platforms:
        print("WARNING: No platforms specified!")
        return

    for platform in platforms:
        platform_runtime_cache = p(runtime_cache, platform)
        print(f"\nProcessing platform: {platform}")
        print(f"Platform directory: {platform_runtime_cache}")

        # Check if directory exists and has files
        needs_download = False
        if not os.path.exists(platform_runtime_cache):
            print(f"Directory does not exist, will create and download...")
            needs_download = True
        else:
            # Check if directory is empty
            contents = os.listdir(platform_runtime_cache)
            if not contents or len(contents) == 0:
                print(f"Directory is empty, will download...")
                needs_download = True
            else:
                print(f"Directory exists with {len(contents)} item(s), skipping download")

        if needs_download:
            if not os.path.exists(platform_runtime_cache):
                os.mkdir(platform_runtime_cache)
            download_platform_runtime(platform_runtime_cache, platform)

    print("\n=== Download process complete ===")


def download_platform_runtime(dir: str, platform: str) -> None:
    print(f"Downloading .NET Core Runtime for platform {platform}.")
    download_file = p(dir, "download.tmp")
    download_url = DOTNET_RUNTIME_DOWNLOADS[platform]

    try:
        print(f"  URL: {download_url}")
        print(f"  Target directory: {dir}")
        print(f"  Temporary file: {download_file}")

        print("  Starting download...")
        urllib.request.urlretrieve(download_url, download_file)

        if not os.path.exists(download_file):
            print(f"  ERROR: File was not created at {download_file}")
            return

        file_size = os.path.getsize(download_file)
        print(f"  Downloaded {file_size} bytes")

        if file_size < 10240:
            try:
                with open(download_file, 'r', errors='ignore') as f:
                    content = f.read()
                    if 'html' in content.lower() or '<!doctype' in content.lower():
                        print(f"  ERROR: Downloaded an HTML file instead of runtime!")
                        print(f"  Content preview: {content[:300]}")
                        os.remove(download_file)
                        return
            except:
                pass

        print(f"  Extracting...")
        if download_url.endswith(".tar.gz"):
            # this is a tar gz.
            with tarfile.open(download_file, "r:gz") as tar:
                tar.extractall(dir)
                print(f"  Successfully extracted tar.gz")
        elif download_url.endswith(".zip"):
            with zipfile.ZipFile(download_file) as zipF:
                zipF.extractall(dir)
                print(f"  Successfully extracted zip")
        else:
            print(f"  ERROR: Unknown file format: {download_url}")
            os.remove(download_file)
            return

        print(f"  Cleaning up temporary file...")
        os.remove(download_file)
        print(f"  Download complete for {platform}")

    except urllib.error.URLError as e:
        print(f"  ERROR: Network error downloading from {download_url}")
        print(f"  Details: {e}")
        if os.path.exists(download_file):
            os.remove(download_file)
    except tarfile.TarError as e:
        print(f"  ERROR: Failed to extract tar file: {e}")
        if os.path.exists(download_file):
            os.remove(download_file)
    except zipfile.BadZipFile as e:
        print(f"  ERROR: Failed to extract zip file: {e}")
        if os.path.exists(download_file):
            os.remove(download_file)
    except Exception as e:
        print(f"  ERROR: Unexpected error: {type(e).__name__}: {e}")
        if os.path.exists(download_file):
            os.remove(download_file)


if __name__ == "__main__":
    main()

