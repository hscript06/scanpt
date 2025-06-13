import subprocess
import platform
import locale
from googletrans import Translator
def mostrar_banner():
    print(r"""
*********************************
                           _   
 ___  ___ __ _ _ __  _ __ | |_ 
/ __|/ __/ _` | '_ \| '_ \| __|
\__ \ (_| (_| | | | | |_) | |_ 
|___/\___\__,_|_| |_| .__/ \__|
                    |_|        
            
*********************************
""")

mostrar_banner()

def detect_and_set_language():
    languages = {
        'es': 'Español',
        'en': 'English',
        'fr': 'Français',
        'ar': 'العربية',
        'de': 'Deutsch',
        'ro': 'Română',
        'ru': 'Русский',
        'zh-cn': '中文',
        'ja': '日本語'
    }
    system_lang = locale.getdefaultlocale()[0] or 'en'
    system_lang = system_lang.lower()
    detected_lang = system_lang if system_lang in languages else 'en'
    
    translator = Translator()
    question = {
        'es': f"Idioma detectado: {languages[detected_lang]}\n¿Es correcto? (S/N): ",
        'en': f"Detected language: {languages[detected_lang]}\nIs it correct? (Y/N): ",
        'fr': f"Langue détectée: {languages[detected_lang]}\nEst-ce correct? (O/N): ",
        'ar': f"اللغة المكتشفة: {languages[detected_lang]}\nهل هذا صحيح؟ (نعم/لا): ",
        'de': f"Erkannte Sprache: {languages[detected_lang]}\nIst das korrekt? (J/N): ",
        'ro': f"Limba detectată: {languages[detected_lang]}\nEste corect? (D/N): ",
        'ru': f"Обнаружен язык: {languages[detected_lang]}\nЭто правильно? (Д/Н): ",
        'zh-cn': f"检测到的语言: {languages[detected_lang]}\n是否正确？(是/否): ",
        'ja': f"検出された言語: {languages[detected_lang]}\n正しいですか？(はい/いいえ): "
    }.get(detected_lang, f"Detected language: {languages[detected_lang]}\nIs it correct? (Y/N): ")
    
    response = input(question).strip().lower()
    
    if response in ('s', 'si', 'sí', 'y', 'yes', 'o', 'oui', 'نعم', 'j', 'ja', 'д', 'да', '是', 'はい'):
        return detected_lang
    else:
        print("\n".join([f"{i+1}. {lang}" for i, (code, lang) in enumerate(languages.items())]))
        lang_prompt = {
            'es': "Seleccione el número de idioma: ",
            'en': "Select language number: ",
            'fr': "Sélectionnez le numéro de langue: ",
            'ar': "حدد رقم اللغة: ",
            'de': "Sprachnummer auswählen: ",
            'ro': "Selectați numărul limbii: ",
            'ru': "Выберите номер языка: ",
            'zh-cn': "选择语言编号: ",
            'ja': "言語番号を選択: "
        }.get(detected_lang, "Select language number: ")
        
        while True:
            try:
                choice = int(input(lang_prompt))
                if 1 <= choice <= len(languages):
                    return list(languages.keys())[choice-1]
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input. Enter a number.")

LANGUAGE = detect_and_set_language()

def t(key):
    translations = {
        'start_scan': {
            'es': "Vamos a empezar a escanear",
            'en': "Let's start scanning",
            'fr': "Commençons le scan",
            'ar': "لنبدأ المسح",
            'de': "Beginnen wir mit dem Scan",
            'ro': "Să începem scanarea",
            'ru': "Начнем сканирование",
            'zh-cn': "开始扫描",
            'ja': "スキャンを開始します"
        },
        'nmap_installed': {
            'es': "¿Tienes instalado nmap?",
            'en': "Do you have nmap installed?",
            'fr': "Avez-vous nmap installé?",
            'ar': "هل لديك nmap مثبت؟",
            'de': "Ist nmap installiert?",
            'ro': "Ai nmap instalat?",
            'ru': "У вас установлен nmap?",
            'zh-cn': "你安装了nmap吗？",
            'ja': "nmapはインストールされていますか？"
        },
        'invalid_response': {
            'es': "Respuesta no válida. Inténtalo de nuevo.",
            'en': "Invalid response. Please try again.",
            'fr': "Réponse non valide. Veuillez réessayer.",
            'ar': "رد غير صالح. يرجى المحاولة مرة أخرى.",
            'de': "Ungültige Antwort. Bitte versuchen Sie es erneut.",
            'ro': "Răspuns invalid. Vă rugăm să încercați din nou.",
            'ru': "Неверный ответ. Пожалуйста, попробуйте еще раз.",
            'zh-cn': "无效响应。请再试一次。",
            'ja': "無効な応答です。もう一度お試しください。"
        },
        'ready': {
            'es': "Perfecto, ya estaríamos listos",
            'en': "Perfect, we're ready",
            'fr': "Parfait, nous sommes prêts",
            'ar': "ممتاز، نحن جاهزون",
            'de': "Perfekt, wir sind bereit",
            'ro': "Perfect, suntem gata",
            'ru': "Отлично, мы готовы",
            'zh-cn': "完美，我们准备好了",
            'ja': "完璧、準備できました"
        },
        'continue': {
            'es': "Perfecto, entonces seguimos adelante.",
            'en': "Perfect, then let's continue.",
            'fr': "Parfait, alors continuons.",
            'ar': "ممتاز، إذن لنكمل.",
            'de': "Perfekt, dann machen wir weiter.",
            'ro': "Perfect, atunci să continuăm.",
            'ru': "Отлично, тогда продолжим.",
            'zh-cn': "完美，那我们继续吧。",
            'ja': "完璧、それでは続けましょう。"
        },
        'scan_time': {
            'es': "Hora de escanear, si quieres ver los comandos introduce 'ayuda'",
            'en': "Time to scan, if you want to see the commands type 'help'",
            'fr': "Il est temps de scanner, si vous voulez voir les commandes tapez 'aide'",
            'ar': "حان وقت المسح، إذا كنت تريد رؤية الأوامر اكتب 'مساعدة'",
            'de': "Zeit zum Scannen, wenn Sie die Befehle sehen möchten, geben Sie 'hilfe' ein",
            'ro': "Este timpul să scanezi, dacă vrei să vezi comenzile tastează 'ajutor'",
            'ru': "Время сканировать, если вы хотите увидеть команды, введите 'помощь'",
            'zh-cn': "扫描时间，如果要查看命令，请输入 '帮助'",
            'ja': "スキャン時間、コマンドを表示するには「ヘルプ」と入力してください"
        },
        'commands': {
            'es': "Comandos disponibles para escanear con nmap:",
            'en': "Available commands to scan with nmap:",
            'fr': "Commandes disponibles pour scanner avec nmap:",
            'ar': "الأوامر المتاحة للمسح باستخدام nmap:",
            'de': "Verfügbare Befehle zum Scannen mit nmap:",
            'ro': "Comenzi disponibile pentru scanare cu nmap:",
            'ru': "Доступные команды для сканирования с помощью nmap:",
            'zh-cn': "可用于 nmap 扫描的命令：",
            'ja': "nmap でスキャンするための利用可能なコマンド:"
        },
        'command_details': {
            'es': "Escribe al final del comando 'detalles' para obtener más información (ejemplo: ping detalles)",
            'en': "Type 'details' at the end of the command for more info (example: ping details)",
            'fr': "Tapez 'détails' à la fin de la commande pour plus d'informations (exemple: ping détails)",
            'ar': "اكتب 'تفاصيل' في نهاية الأمر لمزيد من المعلومات (مثال: ping تفاصيل)",
            'de': "Geben Sie 'details' am Ende des Befehls ein, um weitere Informationen zu erhalten (Beispiel: ping details)",
            'ro': "Tastați 'detalii' la sfârșitul comenzii pentru mai multe informații (exemplu: ping detalii)",
            'ru': "Введите 'детали' в конце команды для получения дополнительной информации (пример: ping детали)",
            'zh-cn': "在命令末尾输入 '详细' 以获取更多信息（例如：ping 详细）",
            'ja': "コマンドの最後に「詳細」と入力すると、詳細情報が表示されます（例：ping 詳細）"
        },
        'exiting': {
            'es': "Saliendo del programa...",
            'en': "Exiting the program...",
            'fr': "Sortie du programme...",
            'ar': "جاري الخروج من البرنامج...",
            'de': "Programm wird beendet...",
            'ro': "Ieșire din program...",
            'ru': "Выход из программы...",
            'zh-cn': "正在退出程序...",
            'ja': "プログラムを終了しています..."
        },
        'cancel_operation': {
            'es': "Operación cancelada.",
            'en': "Operation cancelled.",
            'fr': "Opération annulée.",
            'ar': "تم إلغاء العملية.",
            'de': "Vorgang abgebrochen.",
            'ro': "Operațiune anulată.",
            'ru': "Операция отменена.",
            'zh-cn': "操作已取消。",
            'ja': "操作がキャンセルされました。"
        },
        'enter_ip': {
            'es': "Introduce la IP o rango para comenzar (o escribe 'cancelar'):",
            'en': "Enter the IP or range to start (or type 'cancel'):",
            'fr': "Entrez l'IP ou la plage pour commencer (ou tapez 'annuler'):",
            'ar': "أدخل عنوان IP أو النطاق للبدء (أو اكتب 'إلغاء'):",
            'de': "Geben Sie die IP oder den Bereich ein, um zu beginnen (oder geben Sie 'abbrechen' ein):",
            'ro': "Introduceți IP-ul sau intervalul pentru a începe (sau tastați 'anulare'):",
            'ru': "Введите IP-адрес или диапазон для начала (или введите 'отмена'):",
            'zh-cn': "输入要扫描的 IP 或范围（或输入 '取消'）：",
            'ja': "開始するにはIPまたは範囲を入力してください（または「キャンセル」と入力してください）:"
        },
        'unknown_command': {
            'es': "Comando no reconocido. Escribe 'ayuda' para ver la lista de comandos.",
            'en': "Command not recognized. Type 'help' to see the command list.",
            'fr': "Commande non reconnue. Tapez 'aide' pour voir la liste des commandes.",
            'ar': "الأمر غير معروف. اكتب 'مساعدة' لرؤية قائمة الأوامر.",
            'de': "Befehl nicht erkannt. Geben Sie 'hilfe' ein, um die Befehlsliste anzuzeigen.",
            'ro': "Comandă necunoscută. Tastați 'ajutor' pentru a vedea lista de comenzi.",
            'ru': "Команда не распознана. Введите 'помощь', чтобы увидеть список команд.",
            'zh-cn': "未识别的命令。输入 '帮助' 查看命令列表。",
            'ja': "コマンドが認識されません。コマンドリストを表示するには「ヘルプ」と入力してください。"
        },
        'detected_os': {
            'es': "Sistema operativo detectado",
            'en': "Detected operating system",
            'fr': "Système d'exploitation détecté",
            'ar': "نظام التشغيل المكتشف",
            'de': "Erkanntes Betriebssystem",
            'ro': "Sistem de operare detectat",
            'ru': "Обнаруженная операционная система",
            'zh-cn': "检测到的操作系统",
            'ja': "検出されたオペレーティングシステム"
        },
        'confirm_os': {
            'es': "¿Tu sistema operativo es",
            'en': "Is your operating system",
            'fr': "Est-ce que votre système d'exploitation est",
            'ar': "هل نظام التشغيل الخاص بك هو",
            'de': "Ist Ihr Betriebssystem",
            'ro': "Este sistemul tău de operare",
            'ru': "Ваша операционная система",
            'zh-cn': "你的操作系统是",
            'ja': "あなたのオペレーティングシステムは"
        },
        'select_os_manually': {
            'es': "¿Qué sistema operativo tienes? Selecciona el número:",
            'en': "What operating system do you have? Select the number:",
            'fr': "Quel système d'exploitation avez-vous ? Sélectionnez le numéro :",
            'ar': "ما هو نظام التشغيل لديك؟ حدد الرقم:",
            'de': "Welches Betriebssystem haben Sie? Wählen Sie die Nummer:",
            'ro': "Ce sistem de operare ai? Selectați numărul:",
            'ru': "Какая у вас операционная система? Выберите номер:",
            'zh-cn': "你使用什么操作系统？选择数字：",
            'ja': "使用しているオペレーティングシステムは何ですか？番号を選択してください:"
        },
        'enter_option': {
            'es': "Opción",
            'en': "Option",
            'fr': "Option",
            'ar': "خيار",
            'de': "Option",
            'ro': "Opțiune",
            'ru': "Опция",
            'zh-cn': "选项",
            'ja': "オプション"
        },
        'installing_nmap': {
            'es': "Instalando nmap...",
            'en': "Installing nmap...",
            'fr': "Installation de nmap...",
            'ar': "جاري تثبيت nmap...",
            'de': "Installiere nmap...",
            'ro': "Se instalează nmap...",
            'ru': "Установка nmap...",
            'zh-cn': "正在安装 nmap...",
            'ja': "nmapをインストールしています..."
        },
        'checking_updates': {
            'es': "Buscando actualizaciones...",
            'en': "Checking for updates...",
            'fr': "Recherche de mises à jour...",
            'ar': "جاري البحث عن التحديثات...",
            'de': "Suche nach Updates...",
            'ro': "Se verifică actualizările...",
            'ru': "Проверка обновлений...",
            'zh-cn': "正在检查更新...",
            'ja': "更新を確認しています..."
        },
        'upgrading': {
            'es': "Actualizando...",
            'en': "Upgrading...",
            'fr': "Mise à jour...",
            'ar': "جاري التحديث...",
            'de': "Aktualisiere...",
            'ro': "Se actualizează...",
            'ru': "Обновление...",
            'zh-cn': "正在升级...",
            'ja': "アップグレード中..."
        },
        'installing_choco': {
            'es': "Instalando Chocolatey...",
            'en': "Installing Chocolatey...",
            'fr': "Installation de Chocolatey...",
            'ar': "جاري تثبيت Chocolatey...",
            'de': "Installiere Chocolatey...",
            'ro': "Se instalează Chocolatey...",
            'ru': "Установка Chocolatey...",
            'zh-cn': "正在安装 Chocolatey...",
            'ja': "Chocolateyをインストールしています..."
        },
        'installing_brew': {
            'es': "Instalando Homebrew...",
            'en': "Installing Homebrew...",
            'fr': "Installation de Homebrew...",
            'ar': "جاري تثبيت Homebrew...",
            'de': "Installiere Homebrew...",
            'ro': "Se instalează Homebrew...",
            'ru': "Установка Homebrew...",
            'zh-cn': "正在安装 Homebrew...",
            'ja': "Homebrewをインストールしています..."
        },
        'invalid_os': {
            'es': "No se ha detectado un sistema operativo válido o no se ha seleccionado una opción válida.",
            'en': "No valid operating system detected or no valid option selected.",
            'fr': "Aucun système d'exploitation valide détecté ou aucune option valide sélectionnée.",
            'ar': "لم يتم اكتشاف نظام تشغيل صالح أو لم يتم تحديد خيار صالح.",
            'de': "Kein gültiges Betriebssystem erkannt oder keine gültige Option ausgewählt.",
            'ro': "Nu a fost detectat niciun sistem de operare valid sau nu a fost selectată nicio opțiune validă.",
            'ru': "Не обнаружена допустимая операционная система или не выбран допустимый вариант.",
            'zh-cn': "未检测到有效的操作系统或未选择有效的选项。",
            'ja': "有効なオペレーティングシステムが検出されないか、有効なオプションが選択されていません。"
        },
        'unknown_linux': {
            'es': "Linux desconocido",
            'en': "Unknown Linux",
            'fr': "Linux inconnu",
            'ar': "Linux غير معروف",
            'de': "Unbekanntes Linux",
            'ro': "Linux necunoscut",
            'ru': "Неизвестный Linux",
            'zh-cn': "未知的 Linux",
            'ja': "不明なLinux"
        },
        'unknown_os': {
            'es': "Desconocido",
            'en': "Unknown",
            'fr': "Inconnu",
            'ar': "غير معروف",
            'de': "Unbekannt",
            'ro': "Necunoscut",
            'ru': "Неизвестно",
            'zh-cn': "未知",
            'ja': "不明"
        },
        'type_exit_to_quit': {
            'es': "Escribe 'salir' para terminar",
            'en': "Type 'exit' to quit",
            'fr': "Tapez 'quitter' pour sortir",
            'ar': "اكتب 'خروج' للإنهاء",
            'de': "Geben Sie 'beenden' ein, um zu beenden",
            'ro': "Tastați 'ieșire' pentru a ieși",
            'ru': "Введите 'выход' для завершения",
            'zh-cn': "输入 '退出' 退出",
            'ja': "「終了」と入力して終了します"
        },
        'ip_command': {
            'es': "Muestra tu dirección IP",
            'en': "Shows your IP address",
            'fr': "Affiche votre adresse IP",
            'ar': "يعرض عنوان IP الخاص بك",
            'de': "Zeigt Ihre IP-Adresse an",
            'ro': "Afișează adresa ta IP",
            'ru': "Показывает ваш IP-адрес",
            'zh-cn': "显示你的IP地址",
            'ja': "あなたのIPアドレスを表示します"
        },
        'ping_command': {
            'es': "Hace ping a un rango para detectar hosts activos",
            'en': "Pings a range to detect active hosts",
            'fr': "Envoie des pings à une plage pour détecter les hôtes actifs",
            'ar': "يقوم بعمل ping لنطاق لاكتشاف الأجهزة النشطة",
            'de': "Pingt einen Bereich, um aktive Hosts zu erkennen",
            'ro': "Face ping unui interval pentru a detecta gazde active",
            'ru': "Пингует диапазон для обнаружения активных хостов",
            'zh-cn': "Ping 一个范围以检测活动主机",
            'ja': "範囲に ping を実行してアクティブなホストを検出します"
        },
        'ports_command': {
            'es': "Escanear puertos abiertos comunes",
            'en': "Scan common open ports",
            'fr': "Scanner les ports ouverts communs",
            'ar': "مسح المنافذ المفتوحة الشائعة",
            'de': "Gängige offene Ports scannen",
            'ro': "Scanează porturile deschise comune",
            'ru': "Сканировать общие открытые порты",
            'zh-cn': "扫描常见的开放端口",
            'ja': "一般的な開放ポートをスキャンします"
        },
        'all_ports_command': {
            'es': "Escanear todos los puertos (1-65535)",
            'en': "Scan all ports (1-65535)",
            'fr': "Scanner tous les ports (1-65535)",
            'ar': "مسح جميع المنافذ (1-65535)",
            'de': "Alle Ports scannen (1-65535)",
            'ro': "Scanează toate porturile (1-65535)",
            'ru': "Сканировать все порты (1-65535)",
            'zh-cn': "扫描所有端口 (1-65535)",
            'ja': "すべてのポートをスキャンします (1-65535)"
        },
        'version_command': {
            'es': "Detectar versiones y servicios en puertos abiertos",
            'en': "Detect versions and services on open ports",
            'fr': "Détecter les versions et services sur les ports ouverts",
            'ar': "الكشف عن الإصدارات والخدمات على المنافذ المفتوحة",
            'de': "Erkennen von Versionen und Diensten auf offenen Ports",
            'ro': "Detectează versiuni și servicii pe porturile deschise",
            'ru': "Обнаруживать версии и службы на открытых портах",
            'zh-cn': "检测开放端口上的版本和服务",
            'ja': "開放ポート上のバージョンとサービスを検出します"
        },
        'os_command': {
            'es': "Detectar sistema operativo del host",
            'en': "Detect host operating system",
            'fr': "Détecter le système d'exploitation de l'hôte",
            'ar': "الكشف عن نظام تشغيل المضيف",
            'de': "Betriebssystem des Hosts erkennen",
            'ro': "Detectează sistemul de operare al gazdei",
            'ru': "Определить операционную систему хоста",
            'zh-cn': "检测主机操作系统",
            'ja': "ホストのオペレーティングシステムを検出します"
        },
        'vuln_command': {
            'es': "Escanear vulnerabilidades con scripts NSE",
            'en': "Scan vulnerabilities with NSE scripts",
            'fr': "Scanner les vulnérabilités avec les scripts NSE",
            'ar': "مسح الثغرات الأمنية باستخدام نصوص NSE",
            'de': "Schwachstellen mit NSE-Skripten scannen",
            'ro': "Scanează vulnerabilitățile cu scripturi NSE",
            'ru': "Сканировать уязвимости с помощью скриптов NSE",
            'zh-cn': "使用 NSE 脚本扫描漏洞",
            'ja': "NSEスクリプトで脆弱性をスキャンします"
        },
        'udp_command': {
            'es': "Escanear puertos UDP",
            'en': "Scan UDP ports",
            'fr': "Scanner les ports UDP",
            'ar': "مسح منافذ UDP",
            'de': "UDP-Ports scannen",
            'ro': "Scanează porturile UDP",
            'ru': "Сканировать UDP-порты",
            'zh-cn': "扫描 UDP 端口",
            'ja': "UDPポートをスキャンします"
        },
        'aggressive_command': {
            'es': "Escaneo agresivo con detección extendida",
            'en': "Aggressive scan with extended detection",
            'fr': "Scan agressif avec détection étendue",
            'ar': "مسح عدواني مع الكشف الموسع",
            'de': "Aggressiver Scan mit erweiterter Erkennung",
            'ro': "Scanare agresivă cu detectare extinsă",
            'ru': "Агрессивное сканирование с расширенным обнаружением",
            'zh-cn': "具有扩展检测功能的主动扫描",
            'ja': "拡張検出を伴う積極的なスキャン"
        },
        'traceroute_command': {
            'es': "Hacer traceroute al host",
            'en': "Perform traceroute to the host",
            'fr': "Effectuer un traceroute vers l'hôte",
            'ar': "تنفيذ traceroute إلى المضيف",
            'de': "Traceroute zum Host durchführen",
            'ro': "Efectuează traceroute către gazdă",
            'ru': "Выполнить трассировку до хоста",
            'zh-cn': "对主机执行 traceroute",
            'ja': "ホストへのtracerouteを実行します"
        },
        'firewall_command': {
            'es': "Detectar firewall o filtrado de paquetes",
            'en': "Detect firewall or packet filtering",
            'fr': "Détecter le pare-feu ou le filtrage de paquets",
            'ar': "الكشف عن جدار الحماية أو تصفية الحزم",
            'de': "Firewall oder Paketfilterung erkennen",
            'ro': "Detectează firewall sau filtrarea de pachete",
            'ru': "Обнаружить брандмауэр или фильтрацию пакетов",
            'zh-cn': "检测防火墙或数据包过滤",
            'ja': "ファイアウォールまたはパケットフィルタリングを検出します"
        },
        'slow_scan_command': {
            'es': "Escaneo más sigiloso",
            'en': "Stealthier scan",
            'fr': "Scan plus furtif",
            'ar': "مسح أكثر تخفياً",
            'de': "Unauffälligerer Scan",
            'ro': "Scanare mai discretă",
            'ru': "Более скрытное сканирование",
            'zh-cn': "更隐蔽的扫描",
            'ja': "よりステルスなスキャン"
        },
        'fast_scan_command': {
            'es': "Solo puertos más comunes",
            'en': "Only most common ports",
            'fr': "Seulement les ports les plus courants",
            'ar': "فقط المنافذ الأكثر شيوعًا",
            'de': "Nur die häufigsten Ports",
            'ro': "Doar porturile cele mai comune",
            'ru': "Только самые распространенные порты",
            'zh-cn': "仅最常见的端口",
            'ja': "最も一般的なポートのみ"
        },
        'http_script_command': {
            'es': "Escanear vulnerabilidades HTTP",
            'en': "Scan HTTP vulnerabilities",
            'fr': "Scanner les vulnérabilités HTTP",
            'ar': "مسح ثغرات HTTP",
            'de': "HTTP-Schwachstellen scannen",
            'ro': "Scanează vulnerabilitățile HTTP",
            'ru': "Сканировать уязвимости HTTP",
            'zh-cn': "扫描 HTTP 漏洞",
            'ja': "HTTPの脆弱性をスキャンします"
        },
        'ssh_script_command': {
            'es': "Analizar servicios SSH",
            'en': "Analyze SSH services",
            'fr': "Analyser les services SSH",
            'ar': "تحليل خدمات SSH",
            'de': "SSH-Dienste analysieren",
            'ro': "Analizează serviciile SSH",
            'ru': "Анализировать службы SSH",
            'zh-cn': "分析 SSH 服务",
            'ja': "SSHサービスを分析します"
        },
        'ssl_script_command': {
            'es': "Ver certificados SSL",
            'en': "View SSL certificates",
            'fr': "Voir les certificats SSL",
            'ar': "عرض شهادات SSL",
            'de': "SSL-Zertifikate anzeigen",
            'ro': "Vizualizează certificatele SSL",
            'ru': "Просмотреть SSL-сертификаты",
            'zh-cn': "查看 SSL 证书",
            'ja': "SSL証明書を表示します"
        },
        'dns_script_command': {
            'es': "Escaneo DNS",
            'en': "DNS scan",
            'fr': "Scan DNS",
            'ar': "مسح DNS",
            'de': "DNS-Scan",
            'ro': "Scanare DNS",
            'ru': "Сканирование DNS",
            'zh-cn': "DNS 扫描",
            'ja': "DNSスキャン"
        },
        'smb_script_command': {
            'es': "Buscar recursos compartidos SMB",
            'en': "Search for SMB shares",
            'fr': "Rechercher des partages SMB",
            'ar': "البحث عن مشاركات SMB",
            'de': "Nach SMB-Freigaben suchen",
            'ro': "Caută partajări SMB",
            'ru': "Поиск общих ресурсов SMB",
            'zh-cn': "搜索 SMB 共享",
            'ja': "SMB共有を検索します"
        },
        'whois_command': {
            'es': "Obtener información WHOIS",
            'en': "Get WHOIS information",
            'fr': "Obtenir des informations WHOIS",
            'ar': "الحصول على معلومات WHOIS",
            'de': "WHOIS-Informationen abrufen",
            'ro': "Obține informații WHOIS",
            'ru': "Получить информацию WHOIS",
            'zh-cn': "获取 WHOIS 信息",
            'ja': "WHOIS情報を取得します"
        },
        'ids_evasion_command': {
            'es': "Evadir IDS con señuelos",
            'en': "Evade IDS with decoys",
            'fr': "Éviter les IDS avec leurres",
            'ar': "تجنب أنظمة كشف التسلل باستخدام الطعوم",
            'de': "IDS mit Ködern umgehen",
            'ro': "Evadează IDS-uri cu momele",
            'ru': "Обход IDS с помощью ложных целей",
            'zh-cn': "使用诱饵规避 IDS",
            'ja': "デコイを使用してIDSを回避します"
        },
        'fragmented_command': {
            'es': "Escaneo con paquetes fragmentados",
            'en': "Scan with fragmented packets",
            'fr': "Scanner avec des paquets fragmentés",
            'ar': "مسح مع حزم مجزأة",
            'de': "Scan mit fragmentierten Paketen",
            'ro': "Scanează cu pachete fragmentate",
            'ru': "Сканирование с фрагментированными пакетами",
            'zh-cn': "使用分段数据包扫描",
            'ja': "フラグメント化されたパケットでスキャンします"
        },
        'banner_command': {
            'es': "Obtener banners de servicios",
            'en': "Get service banners",
            'fr': "Obtenir les bannières de service",
            'ar': "الحصول على لافتات الخدمة",
            'de': "Dienst-Banner abrufen",
            'ro': "Obține bannere de serviciu",
            'ru': "Получить баннеры служб",
            'zh-cn': "获取服务横幅",
            'ja': "サービスのバナーを取得します"
        },
        'ipv6_command': {
            'es': "Escanear direcciones IPv6",
            'en': "Scan IPv6 addresses",
            'fr': "Scanner les adresses IPv6",
            'ar': "مسح عناوين IPv6",
            'de': "IPv6-Adressen scannen",
            'ro': "Scanează adrese IPv6",
            'ru': "Сканировать адреса IPv6",
            'zh-cn': "扫描 IPv6 地址",
            'ja': "IPv6アドレスをスキャンします"
        },
        'ifconfig_command': {
            'es': "Mostrar información de red",
            'en': "Show network information",
            'fr': "Afficher les informations réseau",
            'ar': "عرض معلومات الشبكة",
            'de': "Netzwerkinformationen anzeigen",
            'ro': "Afișează informații despre rețea",
            'ru': "Показать сетевую информацию",
            'zh-cn': "显示网络信息",
            'ja': "ネットワーク情報を表示します"
        }
    }
    return translations.get(key, {}).get(LANGUAGE, key)

def pregunta():
    return input("(S/N): ")

def respuesta():
    entrada = pregunta()
    if entrada.lower() in ["s", "si", "y", "yes", "o", "oui", "نعم", "j", "ja", "д", "да", "是", "はい"]:
        return "si"
    elif entrada.lower() in ["n", "no", "n", "non", "لا", "nein", "н", "нет", "否", "いいえ"]:
        return "no"
    else:
        print(t('invalid_response'))
        return respuesta()

def detectar_sistema_operativo():
    so = platform.system()
    if so == "Linux":
        try:
            resultado = subprocess.run(["lsb_release", "-d"], capture_output=True, text=True)
            if resultado.returncode == 0:
                descripcion = resultado.stdout.lower()
                if "arch" in descripcion or "manjaro" in descripcion:
                    return "Arch Linux / Manjaro"
                elif any(x in descripcion for x in ["fedora", "red hat", "rhel", "centos"]):
                    return "Fedora / RHEL / CentOS"
                elif any(x in descripcion for x in ["debian", "ubuntu"]):
                    return "Distribución basada en Debian/Ubuntu"
        except Exception:
            pass

        try:
            with open("/etc/os-release", "r") as f:
                contenido = f.read().lower()
                if "arch" in contenido or "manjaro" in contenido:
                    return "Arch Linux / Manjaro"
                elif any(x in contenido for x in ["fedora", "red hat", "rhel", "centos"]):
                    return "Fedora / RHEL / CentOS"
                elif any(x in contenido for x in ["debian", "ubuntu"]):
                    return "Distribución basada en Debian/Ubuntu"
        except Exception:
            pass
        return t('unknown_linux')
    elif so == "Windows":
        return "Windows"
    elif so == "Darwin":
        return "macOS"
    else:
        return t('unknown_os')

print(t('start_scan'))
print(t('nmap_installed'))
respuesta1 = respuesta()

if respuesta1 == "no":
    os_detectado = detectar_sistema_operativo()
    if os_detectado:
        print(t('detected_os') + f": {os_detectado}")
        print(t('confirm_os') + f" {os_detectado}?")
        respuesta2 = respuesta()
        if respuesta2 != "si":
            os_detectado = None

    if not os_detectado or os_detectado == t('unknown_os'):
        print(t('select_os_manually'))
        print("1--> Arch Linux / Manjaro")
        print("2--> Fedora / RHEL / CentOS")
        print("3--> Fedora/RHEL/CentOS (versiones antiguas)")
        print("4--> Distribución basada en Debian/Ubuntu")
        print("5--> Windows")
        print("6--> MacOS")
        opcion_os = input(t('enter_option') + ": ").strip()
    else:
        if "Arch" in os_detectado:
            opcion_os = "1"
        elif "Fedora" in os_detectado or "RHEL" in os_detectado or "CentOS" in os_detectado:
            opcion_os = "2"
        elif "Debian" in os_detectado or "Ubuntu" in os_detectado:
            opcion_os = "4"
        elif os_detectado == "Windows":
            opcion_os = "5"
        elif os_detectado == "macOS":
            opcion_os = "6"
        else:
            opcion_os = None

    if opcion_os == "1":
        print(t('installing_nmap'))
        subprocess.run(["sudo", "pacman", "-S", "nmap"])
    elif opcion_os == "2" or opcion_os == "3":
        print(t('installing_nmap'))
        subprocess.run(["sudo", "dnf", "install", "nmap"])
    elif opcion_os == "4":
        print(t('checking_updates'))
        subprocess.run(["sudo", "apt", "update"])
        print(t('upgrading'))
        subprocess.run(["sudo", "apt", "upgrade", "-y"])
        print(t('installing_nmap'))
        subprocess.run(["sudo", "apt", "install", "nmap", "-y"])
    elif opcion_os == "5":
        print(t('installing_choco'))
        subprocess.run('powershell -NoProfile -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12; iex ((New-Object System.Net.WebClient).DownloadString(\'https://community.chocolatey.org/install.ps1\'))"', shell=True)
        print(t('installing_nmap'))
        subprocess.run("choco install nmap -y", shell=True)
        subprocess.run("nmap --version", shell=True)
    elif opcion_os == "6":
        print(t('installing_brew'))
        subprocess.run('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"', shell=True)
        print(t('installing_nmap'))
        subprocess.run("brew install nmap", shell=True)
        subprocess.run("nmap --version", shell=True)
    else:
        print(t('invalid_os'))
    
    print(t('ready'))
else:
    print(t('continue'))

print(t('scan_time'))
mostrar_banner()
while True:
    comando = input(">>")
    if comando in ["ayuda", "help", "aide", "مساعدة", "hilfe", "ajutor", "помощь", "帮助", "ヘルプ"]:
        print(t('commands'))
        print(t('command_details'))
        print("1 - ip: " + t('ip_command'))
        print("2 - ping: " + t('ping_command'))
        print("3 - puertos: " + t('ports_command'))
        print("4 - puertos_completo: " + t('all_ports_command'))
        print("5 - version: " + t('version_command'))
        print("6 - sistema_operativo: " + t('os_command'))
        print("7 - vulnerabilidades: " + t('vuln_command'))
        print("8 - udp: " + t('udp_command'))
        print("9 - agresivo: " + t('aggressive_command'))
        print("10 - traceroute: " + t('traceroute_command'))
        print("11 - firewall: " + t('firewall_command'))
        print("12 - escaneo_lento: " + t('slow_scan_command'))
        print("13 - escaneo_rapido: " + t('fast_scan_command'))
        print("14 - script_http: " + t('http_script_command'))
        print("15 - script_ssh: " + t('ssh_script_command'))
        print("16 - script_ssl: " + t('ssl_script_command'))
        print("17 - script_dns: " + t('dns_script_command'))
        print("18 - script_smb: " + t('smb_script_command'))
        print("19 - whois: " + t('whois_command'))
        print("20 - evasión_ids: " + t('ids_evasion_command'))
        print("21 - fragmentado: " + t('fragmented_command'))
        print("22 - banner: " + t('banner_command'))
        print("23 - ipv6: " + t('ipv6_command'))
        print(t('type_exit_to_quit'))

    elif comando in ["salir", "exit", "quitter", "خروج", "beenden", "ieșire", "выход", "退出", "終了"]:
        print(t('exiting'))
        mostrar_banner()
        break

    elif comando == "ip":
        subprocess.run(["ip", "a"])

    elif comando == "ping":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-sn", ip])

    elif comando == "ping detalles":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-v", "-sn", ip])

    elif comando == "puertos":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", ip])

    elif comando == "puertos detalles":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-v", ip])

    elif comando == "puertos_completo":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-p-", ip])

    elif comando == "puertos_completo detalles":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-v", "-p-", ip])

    elif comando == "version":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-sV", ip])

    elif comando == "version detalles":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-v", "-sV", ip])

    elif comando == "sistema_operativo":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["sudo", "nmap", "-O", ip])

    elif comando == "sistema_operativo detalles":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["sudo", "nmap", "-v", "-O", ip])

    elif comando == "vulnerabilidades":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "--script", "vuln", ip])

    elif comando == "vulnerabilidades detalles":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-v", "--script", "vuln", ip])

    elif comando == "udp":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["sudo", "nmap", "-sU", ip])

    elif comando == "udp detalles":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["sudo", "nmap", "-v", "-sU", ip])

    elif comando == "agresivo":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["sudo", "nmap", "-A", ip])

    elif comando == "agresivo detalles":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["sudo", "nmap", "-v", "-A", ip])

    elif comando == "traceroute":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "--traceroute", ip])

    elif comando == "traceroute detalles":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-v", "--traceroute", ip])

    elif comando == "firewall":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-sA", ip])

    elif comando == "firewall detalles":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-v", "-sA", ip])

    elif comando == "escaneo_lento":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-T1", ip])

    elif comando == "escaneo_lento detalles":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-v", "-T1", ip])

    elif comando == "escaneo_rapido":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-T5", "--top-ports", "100", ip])

    elif comando == "escaneo_rapido detalles":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-v", "-T5", "--top-ports", "100", ip])

    elif comando == "script_http":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "--script", "http*", ip])

    elif comando == "script_http detalles":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-v", "--script", "http*", ip])

    elif comando == "script_ssh":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "--script", "ssh*", ip])

    elif comando == "script_ssh detalles":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-v", "--script", "ssh*", ip])

    elif comando == "script_ssl":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "--script", "ssl*", ip])

    elif comando == "script_ssl detalles":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-v", "--script", "ssl*", ip])

    elif comando == "script_dns":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "--script", "dns*", ip])

    elif comando == "script_dns detalles":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-v", "--script", "dns*", ip])

    elif comando == "script_smb":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "--script", "smb*", ip])

    elif comando == "script_smb detalles":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-v", "--script", "smb*", ip])

    elif comando == "whois":
        print(t('enter_domain'))
        dominio = input()
        if dominio.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "--script", "whois-domain", dominio])

    elif comando == "whois detalles":
        print(t('enter_domain'))
        dominio = input()
        if dominio.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-v", "--script", "whois-domain", dominio])

    elif comando == "evasión_ids":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-T1", "-D", "RND:10", ip])

    elif comando == "evasión_ids detalles":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-v", "-T1", "-D", "RND:10", ip])

    elif comando == "fragmentado":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-f", ip])

    elif comando == "fragmentado detalles":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-v", "-f", ip])

    elif comando == "banner":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-sV", "--script", "banner", ip])

    elif comando == "banner detalles":
        print(t('enter_ip'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-v", "-sV", "--script", "banner", ip])

    elif comando == "ipv6":
        print(t('enter_ipv6'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-6", ip])

    elif comando == "ipv6 detalles":
        print(t('enter_ipv6'))
        ip = input()
        if ip.lower() in ["cancelar", "cancel", "annuler", "إلغاء", "abbrechen", "anulare", "отмена", "取消", "キャンセル"]:
            print(t('cancel_operation'))
        else:
            subprocess.run(["nmap", "-v", "-6", ip])

    elif comando == "ip":
        subprocess.run(["ip", "a"])

    elif comando == "ip detalles":
        subprocess.run(["ifconfig"])

    else:
        print(t('unknown_command'))