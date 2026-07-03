# Spectral-X Audio Processor

An advanced audio manipulation tool designed for unique spectral masking, distortion, and custom intro injection.

## Features

- **Spectral Masking**: Implements custom phase-shifting and frequency bin masking to create unique audio signatures.

- **Dynamic Distortion**: Integrated bitcrushing, clipping, and glitch effects for a gritty, industrial feel.

- **Auto-Intro Injection**: Generates a 15.2-second distorted intro with custom text-to-speech (TTS).

- **Temporal Lag**: Adds a natural-feeling lag effect at the start of the track.

## Installation

### Prerequisites

- Python 3.x

- [FFmpeg](https://ffmpeg.org/download.html) (Required for audio processing)

### Setup

```bash
pip install pydub gTTS numpy scipy
```

## Usage

1. Run the script:

   ```bash
   python main.py <path_to_audio_file>
   ```

1. When prompted, enter your desired intro text.

1. The processed file will be saved with a `mod_` prefix in the same directory.

## Disclaimer

This tool is for educational and experimental purposes only.
