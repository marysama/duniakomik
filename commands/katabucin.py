import hikari
import lightbulb
import random
from random import choice

plugin = lightbulb.Plugin('katabucin')


@plugin.command()
@lightbulb.command(
    name="katabucin",
    description="kata bucin.",
)
@lightbulb.implements(lightbulb.SlashCommand)
async def _katabucin(ctx: lightbulb.Context) -> None:
    responses = ["Siapa yang sering ngeluh single mulu tapi gapernah ngasih harapan ke siapapun?",
    "Pernah ga ngerasain putus padahal gapernah pacaran?",
    "Dia nungguin chat darimu itu bukannya karena dia mau bicara sama kamu, tapi karena dia pengen cuekin chat kamu.",
    "Berhentilah memaksa orang yang salah untuk mencintaimu dengan cara yang benar.",
    "dari 'replied to your story' jadi 'being part of your story' itu sesuatu banget.",
    "Umurku ga lagi mengizinkanku sedih karena cinta, jadi kalau kalian lihat aku sedih. itu karena aku gapunya uang.",
    "Inget, kalau sidia mau sama kamu, kamu gaakan single sampai sekarang, jadi move on dong.",
    "Kalau satu pacar aja bisa bikin kamu seneng, bayangin kalau punya 10 biji.",
    "Bayangin kalau kamu bangun tidur, terus disamping kamu ada orang yang paling kamu cintai bilang 'pagi sayang~'. Bayangin aja ya karna sekarang gaakan mungkin kamu ngerasain itu.",
    "Suatu pagi, mengingat namamu sudah tidak terasa sakit. Aku tidak stalk dirimu. Aku tidak merindukanmu. Dan saat itu tiba aku akhirnya bahagia.",
    "Ingat ini, dia akan terus berbohong jika kamu tidak mengetahuinya.",
    "Aku biasanya jarang pacaran tapi sekalinya aku pacaran. Aku malah berpacaran dengan orang yang salah.",
    "Aku malah tertarik pada orang yang tidak memiliki kesempatan untuk bersama sama sekali.",
    "Jadi, kalau aku ga chat kamu duluan, kita gaakan pernah ngobrol?",
    "Ketika kamu bahagia dengan seseorang secara private, kamu gak perlu mengeksposnya di sosmed.",
    "Apa orang yang kamu inginkan menginginkan kamu balik?",
    "Kalau kamu gak bisa menanganiku dalam kondisi terburukku, jangan pacaran denganku karena aku selalu dalam kondisi terburukku.",
    "Tetap jomblo sampai kamu menemukan seseorang, yang akan membuatmu jomblo lagi.",
    "Alasan kenapa kamu belum menemukan belahan jiwamu itu mungkin karena kamu ga punya jiwa.",
    "Aku mungkin kelihatan biasa aja. Tapi, masakanku itu bisa bikin kamu jatuh cinta.",
    "Jangan merasa ditinggalkan, jika ternyata sikapmu sendiri yang membuat seseorang semakin menjauh.",
    "Tahu tempe itu baik, tapi tahu diri jauh lebih baik.",
    "Terkadang, Kamu cuma hanya perlu mendoakan yang terbaik untuk seseorang dan tidak pernah berbicara dengannya lagi.",
    "Apa kamu pernah tertarik dengan suara seseorang?",
    "Tetap merahasiakannya tapi jangan pernah menyangkalnya.",
    "Ketika seorang cewek bilang 'pertama-tama' dalam sebuah argumen, nyerah aja! Karena dia lagi mau nyiapin powerpoint.",
    "Ketika 'rumah' adalah seseorang dan bukan tempat, itulah cinta.",
    "Aku tidak peduli dengan siapa kamu berpacaran dan bermain-main di masa lalu, Kamu terlihat lebih baik denganku.",
    "Dari 'aku beruntung memilikimu' jadi 'kamu pantas mendapatkan seseorang yang lebih baik'.",
    "Jangan minta saran hubungan padaku, aku cuma bot dan aku cuma mendukung perpisahan.",
    "Bayangkan menemukan cinta dan persahabatan dalam satu orang.",
    "Seseorang yang bersabar denganmu adalah salah satu bentuk cinta yang paling lembut.",
    "'Aku tadi lihat mantanmu.' adalah sebuah informasi yang ngga perlu.",
    "Banyak banget pacaran online yang udah putus duluan bahkan sebelum ketemuan.",
    "Tuhan, tolong biarkan aku bersama orang ini selamanya.",
    "Me-reply story adalah cara yang paling bagus buat memulai percakapan.",
    "Kalau kamu mulai suka sama seseorang, tinggal 'sat set sat set' in aja.",
    "Yep, aku percaya kejadian paranormal, karena aku sering mengalami kejadian di ghosting sampe aku gatau dah berapa banyak aku ngalamin itu.",
    "Kalau orang yang kamu deketin tiba-tiba blok kamu, sebenernya yang blok itu pacarnya.",
    "Aku sebenernya lagi gak baik-baik aja, tapi kalau kamu ngajak aku jalan ya kondisiku tiba-tiba baik banget.",
    "Hal yang kuanggap cinta hanyalah kisah sedih.",
    "Aku ingat waktu pertama kita bertemu. Kamu menebar senyum, aku pun terjatuh dalam pandanganmu. Dadaku berdebar. Ya, aku jatuh cinta.",
    "Dan kamu adalah satu-satunya orang yang akan membuat duniaku lebih baik.",
    "Aku sudah cukup bahagia, walau hanya bermimpi tentangmu.",
    "Aku tak tau kapan kita akan bertemu dan melepas rindu. Yang pasti aku akan setia menanti karena aku percaya kamu tak mungkin ingkar janji.",
    "Ketika kamu ingin melepaskan seseorang, kamu harus ingat pertama kali kamu bertemu.",
    "Ketika kamu sudah tidak mencintainya, ingat ketika pertama kali kamu jatuh cinta padanya.",
    "Ketika kamu bosan padanya, ingatlah saat-saat indah kamu bersamanya.",
    "Karena meskipun menyakitkan, aku bisa mencintainya.",
    "Semakin aku mencintaimu, semakin takut aku kehilanganmu.",
    "Aku hanya ingin mencoba memedulikan seseorang, aku mau seseorang itu adalah kamu.",
    "Kamu dengannya saja. Janga tanya padaku tentang kerelaan. Karena jawabannya akan sangat terlihat dari bagaimana beratnya aku melepas kepergianmu.",
    "Apa gunanya mempertahankan seseorang yang hatinya tidak bisa hidup dengan satu orang?",
    "Ia yang kau rindu memang sudah terlampau jauh, karena jaraknya bukan lagi angka, melainkan dekap dari seseorang yang bukan dirimu."]
    await ctx.respond(f"{random.choice(responses)}")


def load(bot):
    bot.add_plugin(plugin)