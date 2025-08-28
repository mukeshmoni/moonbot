#  Moon-Userbot - telegram userbot
#  Copyright (C) 2020-present Moon Userbot Organization
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

from contextlib import redirect_stdout
from io import StringIO

from pyrogram import Client, filters
from pyrogram.types import Message

# noinspection PyUnresolvedReferences
from utils.misc import modules_help, prefix
from utils.scripts import format_exc

# noinspection PyUnresolvedReferences


# noinspection PyUnusedLocal
@Client.on_message(
    filters.command(["ex", "exec", "py", "exnoedit"], prefix) & filters.me
)
async def user_exec(_: Client, message: Message):
    if len(message.command) == 1:
        await message.edit("<b>Code to execute isn't provided</b>")
        return

    code = message.text.split(maxsplit=1)[1]
    stdout = StringIO()

    await message.edit("<b>Executing...</b>")

    try:
        with redirect_stdout(stdout):
            exec(code)  # skipcq
        text = (
            "<b>Code:</b>\n"
            f"<code>{code}</code>\n\n"
            "<b>Result</b>:\n"
            f"<code>{stdout.getvalue()}</code>"
        )
        if message.command[0] == "exnoedit":
            await message.reply(text)
        else:
            await message.edit(text)
    except Exception as e:
        await message.edit(format_exc(e))


# noinspection PyUnusedLocal
@Client.on_message(filters.command(["ev", "eval"], prefix) & filters.me)
async def user_eval(client: Client, message: Message):
    if len(message.command) == 1:
        await message.edit("<b>Code to eval isn't provided</b>")
        return

    code = message.text.split(maxsplit=1)[1]

    try:
        result = eval(code)  # skipcq
        await message.edit(
            "<b>Expression:</b>\n"
            f"<code>{code}</code>\n\n"
            "<b>Result</b>:\n"
            f"<code>{result}</code>"
        )
    except Exception as e:
        await message.edit(format_exc(e))


modules_help["python"] = {
    "ex [python code]": "Execute Python code",
    "exnoedit [python code]": "Execute Python code and return result with reply",
    "eval [python code]": "Eval Python code",
}
