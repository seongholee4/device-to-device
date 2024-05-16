# Device-to-Device Clipboard Sync

This project contains a Python script to send, receive, and monitor clipboard content between devices over a network.

## Features

- **send_clipboard_content**: Sends clipboard content to a specified IP address and port.
- **receive_clipboard_content**: Receives clipboard content from a specified IP address and port.
- **monitor_clipboard**: Monitors the clipboard and sends content to a specified IP address and port whenever the clipboard content changes.

## Usage

1. **Select Mode**: Run the script and choose one of the following modes:
   - `send`
   - `receive`
   - `monitor`

2. **Enter IP Address and Port**: Depending on the chosen mode, enter the required IP address and port.

   - **send**: Requires the target IP address and port to send the clipboard content.
   - **receive**: Requires the listening IP address and port to receive the clipboard content.
   - **monitor**: Requires the target IP address and port to send the clipboard content whenever it changes.

## Example

1. Run the script:

   ```sh
   python device_to_device.py
   ```

2. Choose a mode when prompted:

   ```perl
   Choose mode (send, receive, monitor): send
   ```
 
3. Enter the required IP address and port:

   ```mathematica
   Enter the target IP address: 192.168.1.2
   Enter the target port: 65432
   ```

*This code was generated with the assistance of **ChatGPT 4o**.*