# VeloVision (v0.5 Beta) ⚾🎥

VeloVision is a localized, low-latency delayed video feedback system designed specifically for baseball pitchers during bullpen sessions. By utilizing a wireless catcher-POV camera and a configurable rolling frame buffer, pitchers can throw a pitch and immediately watch their own mechanics without needing a coach to manually record and play back the footage.
## 🚀 What's New in v0.5 Beta

Wireless Catcher POV: Transitioned from wired USB webcams to wireless local IP camera streams.

Standalone Executables: No Python installation required! Pre-compiled binaries are now available for both Windows and Linux.

Threaded Network Capture: Implemented a Producer-Consumer threading model to handle Wi-Fi drops and network stutters silently, preventing the main interface from freezing.

Persistent Configuration: The app automatically remembers your camera URL, delay settings, and playback speeds between sessions.

Dynamic GUI Settings: Change your IP camera URL, delay time, and slow-motion speed on the fly without restarting the application.

## 🛠️ Features

Customizable Time Delay: Set a continuous delay (e.g., 4 seconds) so you can throw, turn to the screen, and watch the pitch arrive.

Instant Replay Mode: Hit Spacebar to instantly pause the live delay and watch the last X seconds of footage in configurable slow-motion (0.1x - 1.0x speed).

Live Recording: Record bullpen sessions directly to .mp4 and save them locally.

Cross-Platform Support: Ready to run on Windows and Linux systems.

## 📋 Hardware Requirements

A computer running the application (placed safely near the mound or backstop).

An iOS/Android smartphone (to be used as the wireless camera).

A tactical chest-rig/harness to securely mount the phone under the catcher's chest protector.

A local Wi-Fi network (both the computer and phone must be connected to the exact same network).

## ⚙️ Quick Start Guide
### 1. Download VeloVision

Head over to the Releases tab on this repository and download the latest executable for your operating system:

Windows: Download the .exe file.

Linux: Download the Linux executable file.

### 2. Start the Wireless Camera (iPhone/Android)

Download IP Camera Lite (or a similar IP webcam app) on your smartphone.

Connect your phone to your local Wi-Fi network.

Open the app and tap Turn on IP Camera Server.

Note the IP address and port displayed on the screen (e.g., http://192.168.1.50:8081).

### 3. Launch the Application

Windows: Double-click the downloaded executable.

Linux: Open your terminal, navigate to your download folder, make the file executable, and run it:

```Bash
chmod +x VeloVision_v0.5
./VeloVision_v0.5
```
(Note: On your very first launch, the video screen will be black because no camera URL is configured yet.)
### 4. Configure the Stream

In the VeloVision app, click Settings > Preferences in the top menu bar.

In the Wireless Camera URL field, enter your phone's IP address.

Crucial Formatting Note: For a stable connection, format the URL exactly like this to include the default app credentials:
http://admin:admin@YOUR_IPV4_ADDRESS:PORT/video
(Example: http://admin:admin@192.168.1.50:8081/video)

Adjust your Delay (Seconds) and Replay Speed.

Click Apply Settings. The stream will initialize and auto-save your setup for your next bullpen.

## ⌨️ Controls

Spacebar - Trigger Instant Replay (Slow-motion playback of the recent buffer). Press again to cancel and return to the live delay.

F - Toggle Fullscreen mode.

Q - Safely quit the application and close network threads.

Record Button - Click the REC button in the UI to start saving the live feed. Go to File > Save Recording... when finished to export the .mp4.

## 💻 For Developers

If you want to pull the repository and run or compile the raw Python scripts yourself:

### Dependencies:
```
Python 3.8+

opencv-python

Pillow

tkinter
```
### Linux Setup (Fedora/RHEL):
You may need to install the underlying system GUI libraries for Tkinter to render the video frames properly before running the .py script:

```Bash
dnf install python3-tkinter tk-devel python3-pillow-tk
pip install opencv-python Pillow
```
### Project Structure:

VeloVision.py: The main GUI application and delay buffer logic.

threaded_camera.py: The asynchronous background network capture class.

velovision_config.json: Auto-generated configuration save file.
