import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

SUPPORT_USERNAME = os.getenv("SUPPORT_USERNAME")
PROMO_CODE = os.getenv("PROMO_CODE")
CHANNEL_LINK = os.getenv("TARGET_CHANNEL")


class Localization:
    def __init__(
            self,
            link: str,
            link_text: str,
            greeting_welcome_start: str,
            greeting_welcome_end: str,
            telegram_channel_text,
            subscribe: str,
            already_subscribed: str,
            error_subscription:str,
            subscriber: str,
            how_does_the_bot_work: str,
            gift: str,
            start_earning: str,
            register_text_1: str,
            register_text_2: str,
            register_button: str,
            get_signal_button: str,
            send_screenshot_button_text: str,
            check_permission_button: str,
            verification_info_message_text: str,
            no_permission_text: str,
            contact_support_button: str,
            open_ios_text: str,
            open_android_text: str,
            webapp: str,
            push
    ):
        self.link = link
        self.link_text = link_text,
        self.greeting_welcome_start = greeting_welcome_start,
        self.greeting_welcome_end = greeting_welcome_end,
        self.telegram_channel_text = telegram_channel_text,
        self.subscribe = subscribe,
        self.already_subscribed=already_subscribed,
        self.error_subscription=error_subscription,
        self.subscriber = subscriber,
        self.how_does_the_bot_work = how_does_the_bot_work
        self.gift = gift,
        self.start_earning = start_earning,
        self.register_text_1=register_text_1,
        self.register_text_2=register_text_2,
        self.register_button = register_button,
        self.get_signal_button = get_signal_button,
        self.send_screenshot_button_text = send_screenshot_button_text,
        self.check_permission_button = check_permission_button,
        self.verification_info_message_text = verification_info_message_text,
        self.no_permission_text = no_permission_text,
        self.contact_support_button = contact_support_button,
        self.open_ios_text = open_ios_text,
        self.open_android_text = open_android_text,
        self.webapp = webapp,
        self.push = push

GREETING_1="Welcome"
GREETING_2=("ready to earn money? 💰\n "
            "To use this bot, subscribe to the channel:\n"
            f"➡️<a href='{CHANNEL_LINK}' style='text-decoration:none'>TELEGRAM CHANNEL LINK</a>⬅️"
            )

LOCALE = {
    'ind_en': Localization(
        link="https://1wdgx.com/casino/list?open=register&p=ytio",
        link_text="1WIN",
        greeting_welcome_start="Welcome, ",
        greeting_welcome_end="ready to earn money? 💰\n "
                             "To use this bot, subscribe to the channel:\n"
                             f"➡️<a href='{CHANNEL_LINK}' style='text-decoration:none'>TELEGRAM CHANNEL LINK</a>⬅️",
        telegram_channel_text="",
        subscribe="Subscribe",
        already_subscribed="Already subscribed ✅",
        error_subscription="Error! You have not subscribed to the channel.",
        subscriber="Great, you have subscribed to the channel.",
        how_does_the_bot_work="How does the bot work? 🤖",
        gift="For the bot to work correctly, the minimum bet is ₹500-1000₹",
        start_earning="Start earning money 💰",
        register_text_1="The rules are simple:\n\n "
                      f"1. Register a 1WIN account using my link and promo code {PROMO_CODE} (press on the link below)\n",
        register_text_2="(The bot only works with a promotional code)\n\n"
                        "2. Make a deposit to 1WIN of at least ₹500-1000₹\n"
                        "(The bot only works for real money)\n\n"
                        "3. After successfully registering and making a deposit, send screenshot to\n"
                        f"{SUPPORT_USERNAME}",
        register_button="REGISTER HERE 🚀",
        get_signal_button="GET SIGNAL 🤖",
        send_screenshot_button_text="SEND SCREENSHOT",
        check_permission_button="CHECK PERMISSION ✅",
        verification_info_message_text=f"Send a screenshot of tour 1WIN account to {SUPPORT_USERNAME} to get access to the bot 🔑\n "
                                       "(Only send screenshot AFTER you've made a deposit to 1WIN)",
        no_permission_text="Error, you don't have an access ti the bot.\n "
                           "Contact support to resolve a problem.",
        contact_support_button="CONTACT SUPPORT 🧑‍💻",
        open_ios_text="Open Web App iOS",
        open_android_text="Open Android | Windows",
        webapp="WEB App:",
        push="PUSH",
    ),
    'ind_hi': Localization(
        link="https://1wdgx.com/casino/list?open=register&p=ytio",
        link_text="1WIN",
        greeting_welcome_start="Swāgat hai, ",
        greeting_welcome_end="paisā kamāne ke liye taiyār hain? 💰\n"
                             "Is bot ko istemāl karne ke liye, channel ko subscribe karein:",
        telegram_channel_text="",
        subscribe="Subscribe karein",
        error_subscription="Error! Aapne channel ko subscribe nahi kiya hai.",
        already_subscribed="pahle se sadasyata li gayi ✅",
        subscriber="Shābāsh! Aapne channel ko subscribe kar liya hai.",
        how_does_the_bot_work="Bot kaise kār kartā hai? 🤖",
        gift="Bot ko thik se kām karne ke liye minimum bet ₹500-1000₹ hai",
        start_earning="Paise kamāna shurū karein 💰",
        register_text_1="Niym saral hain:\n\n"
                        f"1. Mere link aur promo code {PROMO_CODE} ka upyog karte hue 1WIN account banāen (link niche dabāyain)\n",
        register_text_2="(Bot sirf promotional code ke sāth kām kartā hai)\n\n"
                        "2. 1WIN par ₹500-1000₹ kī minimum deposit karein\n"
                        "(Bot sirf real money ke liye kām kartā hai)\n\n"
                        "3. Register aur deposit karne ke bād, screenshot bhejein\n"
                        f"{SUPPORT_USERNAME} ko",
        register_button="REGISTER YAHAN 🚀",
        get_signal_button="SIGNAL PRAAPT KARO 🤖",
        send_screenshot_button_text="SCREENSHOT BHEJEIN",
        check_permission_button="PERMISSION CHECK KARO ✅",
        verification_info_message_text=f"1WIN account ka screenshot {SUPPORT_USERNAME} ko bhejein bot access ke liye 🔑\n"
                                       "(Sirf screenshot bhejein jab aapne 1WIN par deposit kar liya ho)",
        no_permission_text="Error, aapko bot tak pahunch nahi hai.\n"
                           "Samasyā ke liye support se sampark karein.",
        contact_support_button="SUPPORT SE SAMPARK KAREIN 🧑‍💻",
        open_ios_text="Web App iOS Kholo",
        open_android_text="Android | Windows Kholo",
        webapp="WEB App:",
        push="PUSH",
    ),
    'uz': Localization(
        link="https://1wayto.life/casino/list?open=register&p=6mqq",
        link_text="1WIN",
        greeting_welcome_start="Xush kelibsiz, ",
        greeting_welcome_end="pul ishlashga tayyormisiz? 💰\n"
                             "Bu botdan foydalanish uchun, kanalda obuna bo'ling:",
        telegram_channel_text="",
        subscribe="Obuna bo'lish",
        already_subscribed="Allaqachon obuna bo'lingan ✅",
        error_subscription="Xatolik! Siz kanalga obuna bo'lmadingiz.",
        subscriber="Ajoyib! Siz kanalga obuna bo'ldingiz.",
        how_does_the_bot_work="Bot qanday ishlaydi? 🤖",
        gift="Bot to'g'ri ishlashi uchun minimal tikish $10-15 bo'lishi kerak",
        start_earning="Pul ishlashni boshlang 💰",
        register_text_1="Qoidalar oddiy:\n\n"
                        f"1. Mening havolam va promo kodim {PROMO_CODE} yordamida 1WIN hisobini ro'yxatdan o'tkazing (quyidagi havolani bosing)\n",
        register_text_2="(Bot faqat promo kod bilan ishlaydi)\n\n"
                        "2. 1WIN ga kamida $10-15 depozit qiling\n"
                        "(Bot faqat haqiqiy pul bilan ishlaydi)\n\n"
                        "3. Ro'yxatdan o'tgandan va depozit qilgandan keyin screenshot ni jo'nating\n"
                        f"{SUPPORT_USERNAME} ga",
        register_button="BU YERDA RO'YXATDAN O'TING 🚀",
        get_signal_button="SIGNALNI O'LING 🤖",
        send_screenshot_button_text="SCREENSHOT YUBORING",
        check_permission_button="RUXSATNI TEKSHIRISH ✅",
        verification_info_message_text=f"1WIN hisobingizning screenshotini {SUPPORT_USERNAME} ga yuboring botga kirish uchun 🔑\n"
                                       "(Faqat 1WIN ga depozit qilganingizdan keyin screenshot yuboring)",
        no_permission_text="Xatolik, sizda botga kirish huquqi yo'q.\n"
                           "Muammoni hal qilish uchun supportga murojaat qiling.",
        contact_support_button="SUPPORT BILAN BOG'LANISH 🧑‍💻",
        open_ios_text="Web App iOS ni oching",
        open_android_text="Android | Windows ni oching",
        webapp="WEB App:",
        push="PUSH"
    ),
    'ag': Localization(
        link="https://1wqumw.life/casino/list?open=register&p=suc8",
        link_text="1WIN",
        greeting_welcome_start="Bienvenido, ",
        greeting_welcome_end="¿Listo para ganar dinero? 💰\n"
                             "Para usar este bot, suscríbete al canal:",
        telegram_channel_text="",
        subscribe="Suscribirse",
        already_subscribed="Ya suscrito ✅",
        error_subscription="¡Error! No te has suscrito al canal.",
        subscriber="¡Genial! Te has suscrito al canal.",
        how_does_the_bot_work="¿Cómo funciona el bot? 🤖",
        gift="Para que el bot funcione correctamente, la apuesta mínima es de $10-20",
        start_earning="Comienza a ganar dinero 💰",
        register_text_1="Las reglas son simples:\n\n"
                        f"1. Regístrate en 1WIN usando mi enlace y el código promocional {PROMO_CODE} (presiona el enlace a continuación)\n",
        register_text_2="(El bot solo funciona con un código promocional)\n\n"
                        "2. Realiza un depósito en 1WIN de al menos $10-20\n"
                        "(El bot solo funciona con dinero real)\n\n"
                        "3. Después de registrarte y hacer el depósito, envía una captura de pantalla a\n"
                        f"{SUPPORT_USERNAME}",
        register_button="REGÍSTRATE AQUÍ 🚀",
        get_signal_button="OBTENER SEÑAL 🤖",
        send_screenshot_button_text="ENVIAR CAPTURA",
        check_permission_button="VERIFICAR PERMISO ✅",
        verification_info_message_text=f"Envía una captura de pantalla de tu cuenta de 1WIN a {SUPPORT_USERNAME} para obtener acceso al bot 🔑\n"
                                       "(Solo envía la captura después de haber hecho un depósito en 1WIN)",
        no_permission_text="Error, no tienes acceso al bot.\n"
                           "Contacta al soporte para resolver el problema.",
        contact_support_button="CONTACTAR SOPORTE 🧑‍💻",
        open_ios_text="Abrir Web App iOS",
        open_android_text="Abrir Android | Windows",
        webapp="WEB App:",
        push="PUSH"
    ),
    'ch': Localization(
        link="https://1wbsjy.life/casino/list?open=register&p=sdsj",
        link_text="1WIN",
        greeting_welcome_start="Bienvenido, ",
        greeting_welcome_end="¿Listo para ganar dinero? 💰\n"
                             "Para usar este bot, suscríbete al canal:",
        telegram_channel_text="",
        subscribe="Suscribirse",
        already_subscribed="Ya suscrito ✅",
        error_subscription="¡Error! No te has suscrito al canal.",
        subscriber="¡Genial! Te has suscrito al canal.",
        how_does_the_bot_work="¿Cómo funciona el bot? 🤖",
        gift="Para que el bot funcione correctamente, la apuesta mínima es de $10-20",
        start_earning="Comienza a ganar dinero 💰",
        register_text_1="Las reglas son simples:\n\n"
                        f"1. Regístrate en 1WIN usando mi enlace y el código promocional {PROMO_CODE} (presiona el enlace a continuación)\n",
        register_text_2="(El bot solo funciona con un código promocional)\n\n"
                        "2. Realiza un depósito en 1WIN de al menos $10-20\n"
                        "(El bot solo funciona con dinero real)\n\n"
                        "3. Después de registrarte y hacer el depósito, envía una captura de pantalla a\n"
                        f"{SUPPORT_USERNAME}",
        register_button="REGÍSTRATE AQUÍ 🚀",
        get_signal_button="OBTENER SEÑAL 🤖",
        send_screenshot_button_text="ENVIAR CAPTURA",
        check_permission_button="VERIFICAR PERMISO ✅",
        verification_info_message_text=f"Envía una captura de pantalla de tu cuenta de 1WIN a {SUPPORT_USERNAME} para obtener acceso al bot 🔑\n"
                                       "(Solo envía la captura después de haber hecho un depósito en 1WIN)",
        no_permission_text="Error, no tienes acceso al bot.\n"
                           "Contacta al soporte para resolver el problema.",
        contact_support_button="CONTACTAR SOPORTE 🧑‍💻",
        open_ios_text="Abrir Web App iOS",
        open_android_text="Abrir Android | Windows",
        webapp="WEB App:",
        push="PUSH"
    ),
    'bn': Localization(
        link="https://1wltu.com/casino/list?open=register&p=vd4a",
        link_text="1WIN",
        greeting_welcome_start="Swaagata, ",
        greeting_welcome_end="tumi ki taka kamate prastuta? 💰\n"
                             "Ei bot byabohar korar janya, channel-e subscribe karo:",
        telegram_channel_text="",
        subscribe="Subscribe karo",
        already_subscribed="itimodhye sabscraib kora hoyeche ✅",
        error_subscription="Bhulta! Tumi channel-e subscribe karo ni.",
        subscriber="Darun, tumi channel-e subscribe korecho.",
        how_does_the_bot_work="Bot kibhabe kaj kore? 🤖",
        gift="Bot-er thikbhabe kaj korar jonno, minimum bet 700-100 BDT",
        start_earning="Taka kamano suru karo 💰",
        register_text_1="Niomgulo shohoj:\n\n"
                        f"1. Amar link ebong promo code {PROMO_CODE} bebohar kore 1WIN account khulo (nicher link-e click karo)\n",
        register_text_2="(Bot shudhu promotional code-er shathe kaj kore)\n\n"
                        "2. 1WIN-e 700-100 BDT-er minimum deposit koro\n"
                        "(Bot shudhu real money-er jonno kaj kore)\n\n"
                        "3. Register kore ebong deposit korar por, screenshot pathao\n"
                        f"{SUPPORT_USERNAME} ke",
        register_button="REGISTER KORO 🚀",
        get_signal_button="SIGNAL PAO 🤖",
        send_screenshot_button_text="SCREENSHOT PATHAO",
        check_permission_button="PERMISSION CHECK KORO ✅",
        verification_info_message_text=f"1WIN-er account-er screenshot {SUPPORT_USERNAME} ke pathao bot access-er jonno 🔑\n"
                                       "(Shudhu screenshot pathao jakhon tumi 1WIN-e deposit korecho)",
        no_permission_text="Bhulta, tumi bot-er access payo ni.\n"
                           "Samashya samadhan korte support-er shathe jogajog koro.",
        contact_support_button="SUPPORT-ER SHATHE JOGAJOG KORO 🧑‍💻",
        open_ios_text="Web App iOS kholo",
        open_android_text="Android | Windows kholo",
        webapp="WEB App:",
        push="PUSH"
    ),
    'gh': Localization(
        link="https://1wdld.com/casino/list?open=register&p=j8vq",
        link_text="1WIN",
        greeting_welcome_start="Welcome, ",
        greeting_welcome_end="ready to earn money? 💰\n "
                             "To use this bot, subscribe to the channel:",
        telegram_channel_text="",
        subscribe="Subscribe",
        already_subscribed="Already subscribed ✅",
        error_subscription="Error! You have not subscribed to the channel.",
        subscriber="Great, you have subscribed to the channel.",
        how_does_the_bot_work="How does the bot work? 🤖",
        gift="For the bot to work correctly, the minimum bet is $10-15",
        start_earning="Start earning money 💰",
        register_text_1="The rules are simple:\n\n "
                        f"1. Register a 1WIN account using my link and promo code {PROMO_CODE} (press on the link below)\n",
        register_text_2="(The bot only works with a promotional code)\n\n"
                        "2. Make a deposit to 1WIN of at least $10-15\n"
                        "(The bot only works for real money)\n\n"
                        "3. After successfully registering and making a deposit, send screenshot to\n"
                        f"{SUPPORT_USERNAME}",
        register_button="REGISTER HERE 🚀",
        get_signal_button="GET SIGNAL 🤖",
        send_screenshot_button_text="SEND SCREENSHOT",
        check_permission_button="CHECK PERMISSION ✅",
        verification_info_message_text=f"Send a screenshot of tour 1WIN account to {SUPPORT_USERNAME} to get access to the bot 🔑\n "
                                       "(Only send screenshot AFTER you've made a deposit to 1WIN)",
        no_permission_text="Error, you don't have an access ti the bot.\n "
                           "Contact support to resolve a problem.",
        contact_support_button="CONTACT SUPPORT 🧑‍💻",
        open_ios_text="Open Web App iOS",
        open_android_text="Open Android | Windows",
        webapp="WEB App:",
        push="PUSH"
    ),
    'tr': Localization(
        link="https://1wbpqg.top/casino/list?open=register&p=ycwy",
        link_text="1WIN",
        greeting_welcome_start="Hoş geldiniz, ",
        greeting_welcome_end="para kazanmaya hazır mısınız? 💰\n"
                             "Bu botu kullanmak için kanala abone olun:",
        telegram_channel_text="",
        subscribe="Abone Ol",
        already_subscribed="Zaten abone olundu ✅",
        error_subscription="Hata! Kanala abone olmadınız.",
        subscriber="Harika, kanala abone oldunuz.",
        how_does_the_bot_work="Bot nasıl çalışır? 🤖",
        gift="Botun düzgün çalışması için minimum bahis $10-20'tir",
        start_earning="Para kazanmaya başlayın 💰",
        register_text_1="Kurallar basit:\n\n"
                        f"1. Linkimi ve promo kodu {PROMO_CODE} kullanarak 1WIN hesabı açın (aşağıdaki linke tıklayın)\n",
        register_text_2="(Bot sadece promo kodla çalışır)\n\n"
                        "2. 1WIN'e en az $10-20 depozit yapın\n"
                        "(Bot sadece gerçek parayla çalışır)\n\n"
                        "3. Kayıt olduktan ve depozit yaptıktan sonra, ekran görüntüsünü gönderin\n"
                        f"{SUPPORT_USERNAME}",
        register_button="BURADA KAYDOLUN 🚀",
        get_signal_button="SİNYALİ AL 🤖",
        send_screenshot_button_text="EKRAN GÖRÜNTÜSÜ GÖNDER",
        check_permission_button="İZİNİ KONTROL ET ✅",
        verification_info_message_text=f"1WIN hesabınızın ekran görüntüsünü {SUPPORT_USERNAME} adresine gönderin, bot erişimi için 🔑\n"
                                       "(Sadece 1WIN'e depozit yaptıktan sonra ekran görüntüsü gönderin)",
        no_permission_text="Hata, bot'a erişiminiz yok.\n"
                           "Sorunu çözmek için destek ile iletişime geçin.",
        contact_support_button="DESTEK İLE İLETİŞİME GEÇİN 🧑‍💻",
        open_ios_text="Web App iOS'u Aç",
        open_android_text="Android | Windows'u Aç",
        webapp="WEB App:",
        push="PUSH"
    ),
    'br': Localization(
        link="https://1wfwna.life/casino/list?open=register&p=qfcn",
        link_text="1WIN",
        greeting_welcome_start="Bem-vindo, ",
        greeting_welcome_end="pronto para ganhar dinheiro? 💰\n"
                             "Para usar este bot, inscreva-se no canal:",
        telegram_channel_text="",
        subscribe="Inscreva-se",
        already_subscribed="Já inscrito ✅",
        error_subscription="Erro! Você não se inscreveu no canal.",
        subscriber="Ótimo, você se inscreveu no canal.",
        how_does_the_bot_work="Como funciona o bot? 🤖",
        gift="Para que o bot funcione corretamente, a aposta mínima é de 30-40 BRL",
        start_earning="Comece a ganhar dinheiro 💰",
        register_text_1="As regras são simples:\n\n"
                        f"1. Registre-se em 1WIN usando meu link e código promocional {PROMO_CODE} (clique no link abaixo)\n",
        register_text_2="(O bot só funciona com um código promocional)\n\n"
                        "2. Faça um depósito de pelo menos 30-40 BRL no 1WIN\n"
                        "(O bot só funciona com dinheiro real)\n\n"
                        "3. Após se registrar e fazer o depósito, envie a captura de tela para\n"
                        f"{SUPPORT_USERNAME}",
        register_button="REGISTRE-SE AQUI 🚀",
        get_signal_button="OBTER SINAL 🤖",
        send_screenshot_button_text="ENVIAR CAPTURA DE TELA",
        check_permission_button="VERIFICAR PERMISSÃO ✅",
        verification_info_message_text=f"Envie uma captura de tela da sua conta 1WIN para {SUPPORT_USERNAME} para obter acesso ao bot 🔑\n"
                                       "(Só envie a captura após ter feito um depósito no 1WIN)",
        no_permission_text="Erro, você não tem acesso ao bot.\n"
                           "Entre em contato com o suporte para resolver o problema.",
        contact_support_button="ENTRAR EM CONTATO COM O SUPORTE 🧑‍💻",
        open_ios_text="Abrir Web App iOS",
        open_android_text="Abrir Android | Windows",
        webapp="WEB App:",
        push="PUSH"
    ),
    'np': Localization(
        link="https://www.youtube.com/",
        link_text="1WIN",
        greeting_welcome_start="Swāgat chha, ",
        greeting_welcome_end="timi paisā kamauna tayār chau? 💰\n"
                             "Yo bot prayog garnalai, channel subscribe garna hos:",
        telegram_channel_text="",
        subscribe="Subscribe garna hos",
        already_subscribed="pahile nai sadasyata liieko ✅",
        error_subscription="Truti! Timi channel subscribe gareko chhaina.",
        subscriber="Shābāsh, timi channel subscribe gareko chhau.",
        how_does_the_bot_work="Bot kasari kām garcha? 🤖",
        gift="Bot-lāī sahī tariqale kām garna, minimum bet 800-1500 NPR ho",
        start_earning="Paisā kamauna suru garnu hos 💰",
        register_text_1="Niyamharu saral chhan:\n\n"
                        f"1. Mero link ra promo code {PROMO_CODE} prayog gari 1WIN account kholnus (niche ko link ma click garnu hos)\n",
        register_text_2="(Bot promo code sāthmā mātra kām garcha)\n\n"
                        "2. 1WIN mā at least 800-1500 NPR ko deposit garnu hos\n"
                        "(Bot real money sāthmā mātra kām garcha)\n\n"
                        "3. Saphal rūpmā register ra deposit garepachi, screenshot pathāunu hos\n"
                        f"{SUPPORT_USERNAME} mā",
        register_button="YEHA REGISTER GARNUS 🚀",
        get_signal_button="SIGNAL PRAPT GARNUS 🤖",
        send_screenshot_button_text="SCREENSHOT PATHĀUNU HOS",
        check_permission_button="ANUMATI CHECK GARNUS ✅",
        verification_info_message_text=f"1WIN account ko screenshot {SUPPORT_USERNAME} mā pathāunu hos bot access ko lāgi 🔑\n"
                                       "(Screenshot pathāunu hos jab timīle 1WIN mā deposit gareko chhau)",
        no_permission_text="Truti, timīko bot access chhaina.\n"
                           "Samasyā ko samādhān garna lāgi support mā sampark garnu hos.",
        contact_support_button="SUPPORT KO SAMARK GARNUS 🧑‍💻",
        open_ios_text="Web App iOS kholu hos",
        open_android_text="Android | Windows kholu hos",
        webapp="WEB App:",
        push="PUSH"
    ),
    'pk': Localization(
        link="https://1whfbb.life/casino/list?open=register&p=hmrg",
        link_text="1WIN",
        greeting_welcome_start="Khushāmdīd, ",
        greeting_welcome_end="kya aap paisay kamānay ke liye tayyār hain? 💰\n"
                             "Is bot kā istemāl karne ke liye, channel ko subscribe karain:",
        telegram_channel_text="",
        subscribe="Subscribe karain",
        already_subscribed="pehle hi subscribe kiya hua ✅",
        error_subscription="Ghalti! Aap ne channel ko subscribe nahi kiya.",
        subscriber="Mubarak ho, aap ne channel ko subscribe kar liya.",
        how_does_the_bot_work="Bot kaise kām kartā hai? 🤖",
        gift="Bot ko durust kaam karne ke liye minimum bet 1700-2500 PKR hai",
        start_earning="Paisay kamānay shurū karain 💰",
        register_text_1="Qawāid sāda hain:\n\n"
                        f"1. Meri link aur promo code {PROMO_CODE} ke zariye 1WIN account banayein (neeche diye gaye link par click karein)\n",
        register_text_2="(Bot sirf promo code ke sāth kām kartā hai)\n\n"
                        "2. 1WIN par kam az kam 1700-2500 PKR ka deposit karein\n"
                        "(Bot sirf real money ke liye kām kartā hai)\n\n"
                        "3. Registration aur deposit ke bād, screenshot ko\n"
                        f"{SUPPORT_USERNAME} par bhejein",
        register_button="YAHAN REGISTER KARAIN 🚀",
        get_signal_button="SIGNAL HASIL KARAIN 🤖",
        send_screenshot_button_text="SCREENSHOT BHEJEIN",
        check_permission_button="PERMISSION KO CHECK KARAIN ✅",
        verification_info_message_text=f"Apne 1WIN account ka screenshot {SUPPORT_USERNAME} ko bhejein bot tak access hasil karne ke liye 🔑\n"
                                       "(Screenshot sirf 1WIN par deposit karne ke baad bhejein)",
        no_permission_text="Ghalti, aap ke paas bot tak access nahi hai.\n"
                           "Masla hal karne ke liye support se rabta karain.",
        contact_support_button="SUPPORT SE RABTA KARAIN 🧑‍💻",
        open_ios_text="Web App iOS ko kholain",
        open_android_text="Android | Windows ko kholain",
        webapp="WEB App:",
        push="PUSH"
    ),
    'ru': Localization(
        link="https://1warlo.top/casino/list?open=register&p=n6pk",
        link_text="1WIN",
        greeting_welcome_start="Добро пожаловать, ",
        greeting_welcome_end="готовы зарабатывать деньги? 💰\n"
                             "Чтобы использовать этого бота, подпишитесь на канал:",
        telegram_channel_text="",
        subscribe="Подписаться",
        already_subscribed="Уже подписан ✅",
        error_subscription="Ошибка! Вы не подписались на канал.",
        subscriber="Отлично, вы подписались на канал.",
        how_does_the_bot_work="Как работает бот? 🤖",
        gift="Для корректной работы бота минимальная ставка 1000-1500 РУБ",
        start_earning="Начать зарабатывать деньги 💰",
        register_text_1="Правила просты:\n\n"
                        f"1. Зарегистрируйте аккаунт 1WIN, используя мою ссылку и промокод {PROMO_CODE} (нажмите на ссылку ниже)\n",
        register_text_2="(Бот работает только с промокодом)\n\n"
                        "2. Сделайте депозит на 1WIN минимум на 1000-1500 РУБ\n"
                        "(Бот работает только с реальными деньгами)\n\n"
                        "3. После успешной регистрации и внесения депозита отправьте скриншот\n"
                        f"{SUPPORT_USERNAME}",
        register_button="ЗАРЕГИСТРИРОВАТЬСЯ ЗДЕСЬ 🚀",
        get_signal_button="ПОЛУЧИТЬ СИГНАЛ 🤖",
        send_screenshot_button_text="ОТПРАВИТЬ СКРИНШОТ",
        check_permission_button="ПРОВЕРИТЬ ДОСТУП ✅",
        verification_info_message_text=f"Отправьте скриншот вашего аккаунта 1WIN {SUPPORT_USERNAME}, чтобы получить доступ к боту 🔑\n"
                                       "(Отправляйте скриншот только после того, как вы сделали депозит на 1WIN)",
        no_permission_text="Ошибка, у вас нет доступа к боту.\n"
                           "Обратитесь в поддержку для решения проблемы.",
        contact_support_button="СВЯЗАТЬСЯ С ПОДДЕРЖКОЙ 🧑‍💻",
        open_ios_text="Открыть Web App для iOS",
        open_android_text="Открыть Android | Windows",
        webapp="ВЕБ-приложение:",
        push="PUSH"
    ),
    'esp': Localization(
        link="https://www.youtube.com/",
        link_text="1WIN",
        greeting_welcome_start="Bienvenido, ",
        greeting_welcome_end="¿Listo para ganar dinero? 💰\n"
                             "Para usar este bot, suscríbete al canal:",
        telegram_channel_text="",
        subscribe="Suscribirse",
        already_subscribed="Ya suscrito ✅",
        error_subscription="¡Error! No te has suscrito al canal.",
        subscriber="¡Genial! Te has suscrito al canal.",
        how_does_the_bot_work="¿Cómo funciona el bot? 🤖",
        gift="Para que el bot funcione correctamente, la apuesta mínima es de $10-15",
        start_earning="Comienza a ganar dinero 💰",
        register_text_1="Las reglas son simples:\n\n"
                        f"1. Regístrate en 1WIN usando mi enlace y el código promocional {PROMO_CODE} (presiona el enlace a continuación)\n",
        register_text_2="(El bot solo funciona con un código promocional)\n\n"
                        "2. Realiza un depósito en 1WIN de al menos $10-15\n"
                        "(El bot solo funciona con dinero real)\n\n"
                        "3. Después de registrarte y hacer el depósito, envía una captura de pantalla a\n"
                        f"{SUPPORT_USERNAME}",
        register_button="REGÍSTRATE AQUÍ 🚀",
        get_signal_button="OBTENER SEÑAL 🤖",
        send_screenshot_button_text="ENVIAR CAPTURA",
        check_permission_button="VERIFICAR PERMISO ✅",
        verification_info_message_text=f"Envía una captura de pantalla de tu cuenta de 1WIN a {SUPPORT_USERNAME} para obtener acceso al bot 🔑\n"
                                       "(Solo envía la captura después de haber hecho un depósito en 1WIN)",
        no_permission_text="Error, no tienes acceso al bot.\n"
                           "Contacta al soporte para resolver el problema.",
        contact_support_button="CONTACTAR SOPORTE 🧑‍💻",
        open_ios_text="Abrir Web App iOS",
        open_android_text="Abrir Android | Windows",
        webapp="WEB App:",
        push="PUSH"
    ),
    'en': Localization(
        link="https://www.youtube.com/",
        link_text="1WIN",
        greeting_welcome_start="Welcome, ",
        greeting_welcome_end="ready to earn money? 💰\n "
                             "To use this bot, subscribe to the channel:",
        telegram_channel_text="",
        subscribe="Subscribe",
        already_subscribed="Already subscribed ✅",
        error_subscription="Error! You have not subscribed to the channel.",
        subscriber="Great, you have subscribed to the channel.",
        how_does_the_bot_work="How does the bot work? 🤖",
        gift="For the bot to work correctly, the minimum bet is $10-20",
        start_earning="Start earning money 💰",
        register_text_1="The rules are simple:\n\n "
                        f"1. Register a 1WIN account using my link and promo code {PROMO_CODE} (press on the link below)\n",
        register_text_2="(The bot only works with a promotional code)\n\n"
                        "2. Make a deposit to 1WIN of at least $10-20\n"
                        "(The bot only works for real money)\n\n"
                        "3. After successfully registering and making a deposit, send screenshot to\n"
                        f"{SUPPORT_USERNAME}",
        register_button="REGISTER HERE 🚀",
        get_signal_button="GET SIGNAL 🤖",
        send_screenshot_button_text="SEND SCREENSHOT",
        check_permission_button="CHECK PERMISSION ✅",
        verification_info_message_text=f"Send a screenshot of tour 1WIN account to {SUPPORT_USERNAME} to get access to the bot 🔑\n "
                                       "(Only send screenshot AFTER you've made a deposit to 1WIN)",
        no_permission_text="Error, you don't have an access ti the bot.\n "
                           "Contact support to resolve a problem.",
        contact_support_button="CONTACT SUPPORT 🧑‍💻",
        open_ios_text="Open Web App iOS",
        open_android_text="Open Android | Windows",
        webapp="WEB App:",
        push="PUSH"
    )

}