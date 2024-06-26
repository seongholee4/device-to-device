# Device-to-Device Clipboard Sync

This project contains a Python script to send, receive, and monitor clipboard content between devices over a network.
## Requirements

Ensure you have the following Python packages installed:

```sh
pip install pyperclip
```
- The script also uses the built-in `socket` and `time` modules.

## Features

- **send_clipboard_content**: Sends clipboard content to a specified `IP address` and `port`.
- **receive_clipboard_content**: Receives clipboard content from a specified `IP address` and `port`.
- **monitor_clipboard**: Monitors the clipboard and sends content to a specified `IP address` and `port` whenever the clipboard content changes.

## Usage

1. **Select Mode**: Run the script and choose one of the following modes:
   - `send`
   - `receive`
   - `monitor`
   - `exit`

2. **Enter IP Address and Port**: Depending on the chosen mode, enter the required IP address and port.

   - **send**: Requires the `target IP address` and `port` to send the clipboard content.
   - **receive**: Requires the `listening IP address` and `port` to receive the clipboard content.
   - **monitor**: Requires the `target IP address` and `port` to send the clipboard content whenever it changes.

## Example for `send` mode

1. Run the script:

   ```sh
   python device_to_device.py
   ```

2. Choose a mode when prompted:

   ```perl
   Choose mode (send, receive, monitor, exit): send
   ```
 
3. Enter the required IP address and port:

   ```mathematica
   Enter the target IP address: 192.168.1.2
   Enter the target port: 5000
   ```

## Example for `receive` mode

1. Run the script:

    ```sh
    python device_to_device.py
    ```

2. Choose the `receive` mode when prompted:

    ```perl
    Choose mode (send, receive, monitor, exit): receive
    ```
    
3. Enter the listening IP address and port:

   ```mathematica
   Enter the listening IP address: 0.0.0.0
   Enter the listening port: 5000
   ```

## Example for `monitor` mode
1. Run the script:

    ```sh
    python device_to_device.py
    ```

2. Choose the `monitor` mode when prompted:

    ```perl
    Choose mode (send, receive, monitor, exit): monitor
    ```

3. Enter the target IP address and port:

   ```mathematica
   Enter the target IP address: 192.168.1.2
   Enter the target port: 5000
   ```


<br>

*This code was generated with the assistance of **ChatGPT 4o**.*