from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCDmAFj8LGx51aNhU2gpRX0jaTjKYTSYrvKodBYeviH7g0iB1VBsPCOMAO5lpP8gLny8pA00HVikIvVg_cmOeQUUHu4H8ka-pKAg87xKdRZtFzjd7AcbPLBUTKqy3M02OtvYBtiNQNA5jEtEA-K5rd_nC4iCW6ZDJIbThvNOg-cXkAg6_V8pUZh5V1ZZkVhZesz5HVAhyUpQ5VQQtnrHXfWK34DNEXivLrWm36qrHY3EkzghXd4DYvgIuet2J4KEOFMmJ5tLJZddPBD9fshXr6qPr6xYhMw2wQHpIXdB6wr6MMx0T36Gc9S5b2M37a6SWe0Gg8LxsuOWVNYFKBWMuf1X9XNvAA")
BOT_TOKEN = getenv("BOT_TOKEN", "1888191908:AAHcaQcOiXQdXJIyv80d6SVVgVq2IV7f2Zo")
BOT_NAME = getenv("BOT_NAME", "PATRICIA")
admins = {}
API_ID = int(getenv("API_ID", "3898418"))
API_HASH = getenv("API_HASH", "5a82313211da04d63297bd4de436228c")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "80"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1607847356").split()))
