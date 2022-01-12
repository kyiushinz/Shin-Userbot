from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^D(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BACOT NGENTOTTT!!BAPA LU SURUH RIBUT SAMA GUA**")


@register(outgoing=True, pattern='^E(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAK USAH SOK KERAS GOBLOK!!KENCING MASIH BERDIRI AJA BELAGU**")


@register(outgoing=True, pattern='^F(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MUKA LU SEMUA KAYA KONTOL HAHAHAHA!!**")


@register(outgoing=True, pattern='^I(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KONTOL MASIH BENGKOK AJA BANGGA LU HAHAHAHA!!**")


@register(outgoing=True, pattern='^R(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KONTOL KONTOL APA YANG BESAR?KONTOL LU LAH HAHAHAHA!!**")


@register(outgoing=True, pattern='^T(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BABI!!KONTOL!!NGENTOT!!!**")


@register(outgoing=True, pattern='^U(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BABI LU GOBLOK!!GANTENGAN JUGA GUA HAHAHAHA**")


@register(outgoing=True, pattern='^W(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BABI LU GOBLOK!!CANTIKAN JUGA GUA HAHAHAHA**")


@register(outgoing=True, pattern='^Z(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BACOTAN LU GAK BIKIN GUA TREMOR GOBLOK HAHAHAHA!!**")


@register(outgoing=True, pattern='^K(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**HAI PERKENALKAN NAMA SAYA GAK TAU LUPA!!**")


@register(outgoing=True, pattern='^N(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GIMANA KABAR KAMU SAYANG??APAKAH BAIK?**")


@register(outgoing=True, pattern='^B(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ELEEEHHHH SOK BANGET KEPINTERAN KAMU!!**")


@register(outgoing=True, pattern='^M(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**INI GRUB APA KUBURAN SEPI BANGET ASTAGFIRULLAH!!**")


@register(outgoing=True, pattern='^C(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KAN UDAH GUA BILANG??MAKANYA JANGAN NGEYEL!!**")


@register(outgoing=True, pattern='^S(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAUSAH SOKAP DEH KAMU!!**")


@register(outgoing=True, pattern='^V(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MACAM BAGUS AE LU BEGITU HMM!!**")


@register(outgoing=True, pattern='^J(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MAAF BUKAN JAGOAN HAHAHAHA!!**")


@register(outgoing=True, pattern='^A(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BISMILLAH SLEEP CALL!!😁**")


@register(outgoing=True, pattern='^G(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GANTENG LU BEGITU???**")


@register(outgoing=True, pattern='^Y(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**War War Tai anjing, Ketrigger minta sharelok, Udah di sharelok Ga nyamperin,Keras di sosmed Bhakss...**")


@register(outgoing=True, pattern='^H(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**CANTIK LU BEGITU???**")


@register(outgoing=True, pattern='^O(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MENTANG MENTANG PUNYA BOT MAINNYA BOT!!PANTES MUKANYA KAYA BOT😁**")


CMD_HELP.update({
    "toxic":
    "D\
\nUsage: Bacotin Orang.\
\n\n E\
\nUsage: Buat Orang Yang Sok Keras.\
\n\n F\
\nUsage: Ngatain Orang Wkwkkw.\
\n\n I\
\nUsage: Kontol Orang Ngatain.\
\n\n R\
\nUsage: Pantun Anjing.\
\n\n T\
\nUsage: Nyebutin Binatang.\
\n\n U\
\nUsage: Biar Dikata Ganteng.\
\n\n W\
\nUsage: Biar Dikata Cantik.\
\n\n Z\
\nUsage: Tremor Kan Lu.\
\n\n K\
\nUsage: Memperkenalkan Diri.\
\n\n N\
\nUsage: Menanyakan Kabar.\
\n\n B\
\nUsage: Sok Kepinteran.\
\n\n M\
\nUsage: Gc Nya Kaya kuburan.\
\n\n C\
\nUsage: Dia tuh Ngeyel banget.\
\n\n S\
\nUsage: Haha sokap.\
\n\n V\
\nUsage: Merendah.\
\n\n A\
\nUsage: Nyari Sleep Call.\
\n\n J\
\nUsage: Hujat yang gapunya muka.\
\n\n G\
\nUsage: Kegantengan.\
\n\n Y\
\nUsage: teruntuk petarung.\
\n\n H\
\nUsage: Kecantikan.\
\n\n O\
\nUsage: Ngatain org norak."
})
