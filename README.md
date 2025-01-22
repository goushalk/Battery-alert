# Battery Alert Service

This repository contains a Python-based service that checks the battery level of your system and provides alerts when the battery is low.

---

## Features
- Monitors battery level periodically.
- Sends notifications using `battery` (Linux).
- Automatically runs in the background as a systemd service after system boot.

---

## Prerequisites

Ensure the following are installed on your system:

- **Python 3**
  ```bash
  sudo apt install python3
  ```
- **psutil** (for notifications)
  ```bash
  pip install psutil
  ```

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/goushalk/battery-alert.git
cd battery-alert
```

### 2. Make the Script Executable
```bash
chmod +x battery_alert.py
```

### 3. Set Up as a Systemd Service

1. Create a systemd service file:
   ```bash
   sudo nano /etc/systemd/system/battery_alert.service
   ```
2. Add the following content to the file:
   ```ini
   [Unit]
   Description=Battery Checker Service
   After=network.target

   [Service]
   ExecStart=/usr/bin/python3 /path/to/your/battery_alert.py
   Environment="DISPLAY=:0"
   Environment="XAUTHORITY=/home/<your-username>/.Xauthority"
   WorkingDirectory=/path/to/your
   Restart=always
   User=<your-username>
   Group=<your-username>

   [Install]
   WantedBy=multi-user.target
   ```
   Replace `/path/to/your` and `<your-username>` with the actual path and your username.

3. Reload and start the service:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable battery_alert.service
   sudo systemctl start battery_alert.service
   ```

4. Check the service status:
   ```bash
   sudo systemctl status battery_alert.service
   ```

---

## Usage
The script will run in the background and send notifications whenever the battery level drops below a certain threshold. You can modify the threshold by editing the script.

---

## Debugging
- View logs:
  ```bash
  journalctl -u battery_alert.service
  ```
- Test the script manually:
  ```bash
  python3 battery_alert.py
  ```

---

## Contributing
Feel free to fork the repository and submit a pull request. Suggestions and improvements are welcome!

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Author
Created by [Goushal](https://github.com/goushalk), aka `op11r`.

