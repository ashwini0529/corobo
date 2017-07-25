import re
import string

from errbot import BotPlugin, botcmd


class Pitchfork(BotPlugin):
    """
    To pitchfork users down to ...
    """

    @botcmd
    def pitchfork(self, msg, arg):
        """
        To pitchfork user down to ...
        """
        match = re.match(r'@?([\w-]+)(?:\s+(?:down\s+)?to\s+(.+))?$',
                         arg)
        if match:
            user = match.group(1)
            place = match.group(2) if match.group(2) else 'offtopic'
            return (
                string.Template("""
@$user, you are being pitchforked down to $place
```
                                                         .+====----->
                                                          \('
====================================================<%{%{%{>>+===---> $user
                                                          /(,
                                                         ,+====----->
```
""").substitute(user=user, place=place)
                )
        else:
            return "Usage: `pitchfork user [[down] to place]`"
