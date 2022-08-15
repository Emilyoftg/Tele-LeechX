class TXStyle:
    TOGGLEDOC_MSG = '''┏━━ 🛠  𝗧𝗼𝗴𝗴𝗹𝗲 𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀 :
┃
┣ 👤 𝐔𝐬𝐞𝐫 : {u_men} ( #ID{u_id} )
┃
┣🏷 𝐓𝐨𝐠𝐠𝐥𝐞 : 📁<code>Document 📂</code>
┃
┗━♦️ℙ𝕠𝕨𝕖𝕣𝕖𝕕 𝔹𝕪 {UPDATES_CHANNEL}♦️━╹'''
    TOGGLEVID_MSG = '''┏━━ 🛠  𝗧𝗼𝗴𝗴𝗹𝗲 𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀 :
┃
┣ 👤 𝐔𝐬𝐞𝐫 : {u_men} ( #ID{u_id}
┃
┣🏷𝐓𝐨𝐠𝐠𝐥𝐞 : <code>🎞 Video 🎞</code>
┃
┗━♦️ℙ𝕠𝕨𝕖𝕣𝕖𝕕 𝔹𝕪 {UPDATES_CHANNEL}♦️━╹'''
    SAVETHUMB_REPLY = "<code>Processing . . . 🔄</code>"
    SAVE_THUMB_MSG = "<b>⚡<i>Custom Thumbnail 🖼 Saved for Next Uploads</i>⚡</b>\n\n <b><i>✅Your Photo is Set, Ready to Go ...👨‍🦯</i></b>."
    CLEAR_THUMB_SUCC_MSG = "<b><i>✅Success✅</i></b>\n\n <b>🖼Custom Thumbnail Cleared Successfully As Per Your Request.</b>"
    CLEAR_THUMB_FAIL_MSG = "<b><i>⛔Sorry⛔</i></b>\n\n <b>❌Nothing to Clear For You❌</b>"
    PREFIX_MSG = "⚡️<i><b>Custom Prefix Set Successfully</b></i> ⚡️ \n\n👤 <b>User :</b> {u_men}\n🆔 <b>User ID :</b> <code>{user_id_}</code>\n🗃 <b>Prefix :</b> <code>{txt}</code>"
    CAPTION_MSG = "⚡️<i><b>Custom Caption Set Successfully</b></i> ⚡️ \n\n👤 <b>User :</b> {u_men}\n🆔 <b>User ID :</b> <code>{user_id_}</code>\n🗃 <b>Caption :</b>\n<code>{txt}</code>"
    IMDB_MSG = "⚡️<i><b>Custom Template Set Successfully</b></i> ⚡️ \n\n👤 <b>User :</b> {u_men}\n🆔 <b>User ID :</b> <code>{user_id_}</code>\n🗃 <b>IMDB Template :</b> \n<code>{txt}</code>"
    THEME_MSG = "⚡️ <i><b>Available Custom Themes</b></i> ⚡️\n\n👤 <b>User :</b> {u_men}\n🆔 <b>User ID :</b> <code>{user_id_}</code>\n\n🗄 <b>Choose Available Theme from Below:</b>"
    STATS_MSG_1 = '┏━━━━ 📊 𝗕𝗼𝘁 𝗦𝘁𝗮𝘁𝘀 📊 ━━━━━╻\n'
    STATS_MSG_2 = '┣ 📝 <b>Commit Date:</b> {last_commit}\n┃\n'
    STATS_MSG_3 = '''┣ 🤖 <b>Bot Uptime:</b> {currentTime}\n'
┣ 📶 <b>OS Uptime:</b> {osUptime}
┃
┣ 🗄 <b>Total Disk Space:</b> {total}
┣ 📇 <b>Used:</b> {used} | 🛒 <b>Free:</b> {free}
┃
┣ 📤 <b>Upload:</b> {sent}
┣ 📥 <b>Download:</b> {recv}
┃
┣ 🚦 <b>CPU:</b> {cpuUsage}%
┣ 🧬 <b>RAM:</b> {mem_p}%
┣ 🗃 <b>DISK:</b> {disk}%
┃
┣ 📄 <b>Physical Cores:</b> {p_core}
┣ 📑 <b>Total Cores:</b> {t_core}
┃
┣ 🔁 <b>SWAP:</b> {swap_t} | 🔀 <b>Used:</b> {swap_p}%
┣ 📫 <b>Memory Total:</b> {mem_t}
┣ 📭 <b>Memory Free:</b> {mem_a}
┣ 📬 <b>Memory Used:</b> {mem_u}
┃
┗━♦️ℙ𝕠𝕨𝕖𝕣𝕖𝕕 𝔹𝕪 {UPDATES_CHANNEL}♦️━╹'''
    HELP_MSG = '''┏━ 🆘 <b>HELP MODULE</b> 🆘 ━━━╻
┃
┃• <i>Open Help to Get Tips and Help</i>
┃• <i>Use the Bot Like a Pro User</i>
┃• <i>Access Every Feature That Bot Offers in Better Way </i>
┃• <i>Go through Commands to Get Help</i>
┃
┗━♦️ℙ𝕠𝕨𝕖𝕣𝕖𝕕 𝔹𝕪 {UPDATES_CHANNEL}♦️━╹'''
    INDEX_SCRAPE_MSG = """
┏━📮  𝗜𝗻𝗱𝗲𝘅 𝗦𝗰𝗿𝗮𝗽𝗲 𝗥𝗲𝘀𝘂𝗹𝘁 :
┃
┣👤 𝐔𝐬𝐞𝐫 : {u_men} ( #ID{user_id_} )
┃
┣🔗 𝗨𝗥𝗟 : <code> {url} </code>
┃
┗━♦️ℙ𝕠𝕨𝕖𝕣𝕖𝕕 𝔹𝕪 {UPDATES_CHANNEL}♦️━╹
"""
    MEDIAINFO_MEDIA_MSG = '''
ℹ️ <code>MEDIA INFO</code> ℹ
┃
┃• <b>File Name :</b> <code>{x_media.file_name}</code>
┃• <b>Mime Type :</b> <code>{x_media.mime_type}</code>
┃• <b>File Size :</b> <code>{humanbytes(x_media.file_size)}</code>
┃• <b>Date :</b> <code>{x_media.date}</code>
┃• <b>File ID :</b> <code>{x_media.file_id}</code>
┃• <b>Media Type :</b> <code>{text_}</code>
┃
┗━♦️ℙ𝕠𝕨𝕖𝕣𝕖𝕕 𝔹𝕪 {UPDATES_CHANNEL}♦️━╹
'''
    MEDIAINFO_DIRECT_MSG = """
ℹ️ <code>DIRECT LINK INFO</code> ℹ
┃
┃• <b>File Name :</b> <code>{title}</code>
┃• <b>Direct Link :</b> <code>{link}</code>
┃
┗━♦️ℙ𝕠𝕨𝕖𝕣𝕖𝕕 𝔹𝕪 {UPDATES_CHANNEL}♦️━╹
"""
    SPEEDTEST_MSG = '''
┏━━━━━━━━━━━━━━━━━━╻
┣━━🚀 𝐒𝐩𝐞𝐞𝐝𝐭𝐞𝐬𝐭 𝐈𝐧𝐟𝐨:
┣ <b>Upload:</b> <code>{humanbytes(result['upload'] / 8)}/s</code>
┣ <b>Download:</b>  <code>{humanbytes(result['download'] / 8)}/s</code>
┣ <b>Ping:</b> <code>{result['ping']} ms</code>
┣ <b>Time:</b> <code>{result['timestamp']}</code>
┣ <b>Data Sent:</b> <code>{humanbytes(result['bytes_sent'])}</code>
┣ <b>Data Received:</b> <code>{humanbytes(result['bytes_received'])}</code>
┃
┣━━🌐 𝐒𝐩𝐞𝐞𝐝𝐭𝐞𝐬𝐭 𝐒𝐞𝐫𝐯𝐞𝐫:
┣ <b>Name:</b> <code>{result['server']['name']}</code>
┣ <b>Country:</b> <code>{result['server']['country']}, {result['server']['cc']}</code>
┣ <b>Sponsor:</b> <code>{result['server']['sponsor']}</code>
┣ <b>Latency:</b> <code>{result['server']['latency']}</code>
┣ <b>Latitude:</b> <code>{result['server']['lat']}</code>
┣ <b>Longitude:</b> <code>{result['server']['lon']}</code>
┃
┣━━👤 𝐂𝐥𝐢𝐞𝐧𝐭 𝐃𝐞𝐭𝐚𝐢𝐥𝐬:
┣ <b>IP Address:</b> <code>{result['client']['ip']}</code>
┣ <b>Latitude:</b> <code>{result['client']['lat']}</code>
┣ <b>Longitude:</b> <code>{result['client']['lon']}</code>
┣ <b>Country:</b> <code>{result['client']['country']}</code>
┣ <b>ISP:</b> <code>{result['client']['isp']}</code>
┣ <b>ISP Rating:</b> <code>{result['client']['isprating']}</code>
┃
┗━━━━━━━━━━━━━━━━━━╹
'''
    TSHELP_MSG = '''
┏━ 𝗧𝗼𝗿𝗿𝗲𝗻𝘁 𝗦𝗲𝗮𝗿𝗰𝗵 𝗠𝗼𝗱𝘂𝗹𝗲 ━━╻
┃
┃• /nyaasi <i>[search query]</i>
┃• /sukebei <i>[search query]</i>
┃• /1337x <i>[search query]</i>
┃• /piratebay <i>[search query]</i>
┃• /tgx <i>[search query]</i>
┃• /yts <i>[search query]</i>
┃• /eztv <i>[search query]</i>
┃• /torlock <i>[search query]</i>
┃• /rarbg <i>[search query]</i>
┃• /ts <i>[search query]</i>
┃
┗━♦️ℙ𝕠𝕨𝕖𝕣𝕖𝕕 𝔹𝕪 @FuZionX♦️━╹
'''
