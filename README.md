# Virtual Camera with Background Replacement

## Inspiration
This project was inspired by applications that offer virtual background replacement. The goal was to provide an alternative for cases where such a feature is not available.

## Features
- **Background Replacement**: Replace your webcam background with an image of your choice.
- **Blurred Background**: If no image is provided, a blurred version of the original background is used.
- **Custom Camera Resolution and FPS**: Allows users to specify custom width, height, and FPS for the virtual camera.
- **Virtual Camera Output**: Streams the processed video feed to a virtual camera, which can be used in other applications.

## Requirements
- **OBS Studio**: Required to create the virtual camera. In newer versions of OBS Studio, the default settings should work without additional configuration.

## Usage
1. Install the required dependencies.
2. Ensure that OBS Studio is installed.
3. Run the script with optional arguments:
   ```bash
   python main.py --background path/to/image.jpg --width 1280 --height 720 --fps 30
   ```
4. After launching the script, a new camera source will appear in your system. You can use it in any application by selecting the correct camera source.
