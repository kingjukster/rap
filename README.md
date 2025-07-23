# rap

## Setup

Install the required packages (uses OpenAI SDK version 1.x):

```bash
pip install -r requirements.txt
```

Create a `.env` file in this directory with the following content:

```ini
OPENAI_API_KEY=your-api-key-here
```

## Running

Execute the script manually:

```bash
python generate_rap.py
```

Alternatively, run the helper script to install dependencies and execute the
program in one step:

```bash
./run.sh
```

To install the cron job automatically, pass `--install-cron`:

```bash
./run.sh --install-cron
```

## Schedule with cron

If you prefer to add the job yourself, schedule it to run every 6 hours:

```
0 */6 * * * /usr/bin/python3 /path/to/generate_rap.py
```
