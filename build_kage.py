#!/usr/bin/env python3
"""Build index.html from the byte-exact ThreeUI Kage source (kage.source.html).

Only text content, link targets and the wordmark word are replaced; structure,
CSS, shaders, motion and asset paths stay as authored. The typography sheet the
<KageLandingPage /> frame would append (KAGE_TYPOGRAPHY recipe, configured
props) is added last in <head>, exactly as applyPageCustomization() does.
"""
import re, sys
src = open('kage.source.html', encoding='utf-8').read()
out = src
count = 0
def rep(old, new, n=1):
    global out, count
    c = out.count(old)
    if c != n:
        sys.exit(f'expected {n} occurrence(s), found {c}: {old[:80]!r}')
    out = out.replace(old, new); count += 1

# ---- head
rep('<html lang="en">', '<html lang="ru">')
rep('<title>Kage — Where stillness reveals the unseen</title>', '<title>In Way Tour — Приключения ждут</title>')
rep('<meta name="description" content="A five-chapter night walk through a Kyoto mountain temple. Charred cypress, lantern light and a vermilion moon, rendered live in WebGL.">',
    '<meta name="description" content="In Way Tour — туристическая компания в Ташкенте. Индивидуальные и групповые туры: Турция, ОАЭ, Бали, Таиланд, Египет, Вьетнам, Азербайджан.">')

# ---- preloader
rep('<div class="pre-jp jp">影の道</div>', '<div class="pre-jp jp">IN WAY TOUR</div>')
rep('<span>Raising the mountain temple</span>', '<span>Собираем маршрут</span>')

# ---- nav
rep('<span class="brand-tx"><b>KAGE</b><i>HIDDEN REALMS OF KYOTO</i></span>', '<span class="brand-tx"><b>IN WAY TOUR</b><i>ПУТЕШЕСТВИЯ ПО ВСЕМУ МИРУ</i></span>')
rep('<span>Temples</span><span class="alt">伽藍</span>', '<span>О компании</span><span class="alt">01</span>')
rep('<span>Gardens</span><span class="alt">庭園</span>', '<span>Направления</span><span class="alt">02</span>')
rep('<span>Rituals</span><span class="alt">神事</span>', '<span>Преимущества</span><span class="alt">03</span>')
rep('<span>Afterlight</span><span class="alt">残光</span>', '<span>Контакты</span><span class="alt">04</span>')

# ---- hero
rep('<span class="dot"></span> Chapter 00 — The Hidden Gate', '<span class="dot"></span> Глава 00 — Ташкент, Узбекистан')
rep('<span class="mask-line"><span>Where stillness</span></span>', '<span class="mask-line"><span>Приключения ждут —</span></span>')
rep('<span class="mask-line"><span>reveals the</span></span>', '<span class="mask-line"><span>отправляйтесь</span></span>')
rep('<span class="mask-line"><span>unseen.</span></span>', '<span class="mask-line"><span>с нами.</span></span>')
rep('''Enter Kyoto through its quiet thresholds, where ritual,
      craft, and memory shape the path.''', '''Уникальные маршруты и увлекательные туры, которые
      подарят вам незабываемые эмоции и впечатления.''')
rep('<span>Scroll to enter</span>', '<span>Листайте вниз</span>')
rep('<b>Thresholds</b><p>Discover the hidden gates that open on to deeper paths.</p>', '<b>Индивидуальный подход</b><p>Уникальные маршруты с учётом всех пожеланий клиента.</p>')
rep('<b>Still Gardens</b><p>Witness the courts where silence gently unfolds.</p>', '<b>Профессионализм</b><p>Опытная команда и поддержка на всех этапах путешествия.</p>')
rep('<b>Sacred Craft</b><p>Embrace the hands and heritage that shape devotion.</p>', '<b>Широкий выбор</b><p>От экзотических пляжей до культурных столиц мира.</p>')
rep('<b>Night Rituals</b><p>Explore the rites that awaken when the day is done.</p>', '<b>Онлайн-оплата</b><p>Выберите тур и оплатите через защищённый платёжный портал.</p>')
rep('aria-label="Preview: Sanmon, before the bell"', 'aria-label="Превью: живая сцена, перейти к направлениям"')
rep('<span class="peek-cap"><b class="jp">山門</b><i>Sanmon — before the bell</i></span>', '<span class="peek-cap"><b class="jp">3D</b><i>Живая сцена — к направлениям</i></span>')
rep('<div class="word-fb" aria-hidden="true">KAGE</div>', '<div class="word-fb" aria-hidden="true">IN WAY</div>')
rep('<span class="v jp">影の道</span>', '<span class="v jp">IN WAY TOUR</span>')

# ---- 01 about
rep('<span class="k"><b>01</b> — The Sanmon</span><span class="rule"></span><span class="k jp">山門</span>', '<span class="k"><b>01</b> — О компании</span><span class="rule"></span><span class="k jp">ABOUT</span>')
rep('Charred cypress, worn stone, one gate left open.', 'Воспоминания о будущем забронированы здесь.')
rep('''Kage begins where the city stops: a mountain gate of cedar burned black,
        standing in its own weather. The soot is not decoration. It is how a board is taught to survive a
        hundred rainy seasons, and the first thing this place asks you to understand.''',
    '''С In Way Tour ваши будущие воспоминания уже ждут вас. Мы предлагаем незабываемые
        путешествия в самые удивительные уголки мира. Каждый тур разрабатывается индивидуально, чтобы
        подарить вам уникальные впечатления и эмоции.''')
rep('''Climb the worn steps and the worship hall lifts out of the mist, its paper
        screens lit from inside like a lantern the size of a house. Above the eaves a vermilion moon holds
        its place, patient, half hidden. Nothing here is in a hurry. Neither, for the next ninety minutes,
        are you.''',
    '''In Way Tour — ведущая туристическая компания, специализирующаяся на организации
        эксклюзивных путешествий по всему миру. Индивидуальные и групповые туры, корпоративные поездки,
        тематические путешествия — только с надёжными партнёрами и на лучших условиях. Директор и
        основатель компании — Ходжиматова Мохизодхон Бахтияровна.''')
rep('<span>Cross the threshold</span>', '<span>Смотреть направления</span>')
rep('<div><b>05</b><span>Chapters</span></div>', '<div><b>5+</b><span>Лет опыта</span></div>')
rep('<div><b>92</b><span>Minutes</span></div>', '<div><b>9</b><span>Направлений</span></div>')
rep('<div><b>1611</b><span>Hall raised</span></div>', '<div><b>6</b><span>Программ туров</span></div>')
rep('<div><b>∞</b><span>Stillness</span></div>', '<div><b>∞</b><span>Впечатлений</span></div>')

# ---- 02 destinations
rep('<span class="k"><b>02</b> — Still Gardens</span><span class="rule"></span><span class="k jp">庭園</span>', '<span class="k"><b>02</b> — Направления</span><span class="rule"></span><span class="k jp">TOURS</span>')
rep('<div class="card-lab"><b>Approach</b><span class="jp">参道</span></div>', '<div class="card-lab"><b>Стамбул</b><span class="jp">TR</span></div>')
rep('<div class="card-meta"><span>The long climb</span><span>01 / 03</span></div>', '<div class="card-meta"><span>Турция</span><span>01 / 03</span></div>')
rep('<div class="card-lab"><b>Lanterns</b><span class="jp">灯籠</span></div>', '<div class="card-lab"><b>Дубай</b><span class="jp">AE</span></div>')
rep('<div class="card-meta"><span>Lantern court</span><span>02 / 03</span></div>', '<div class="card-meta"><span>ОАЭ</span><span>02 / 03</span></div>')
rep('<div class="card-lab"><b>Moonwater</b><span class="jp">月影</span></div>', '<div class="card-lab"><b>Бали</b><span class="jp">ID</span></div>')
rep('<div class="card-meta"><span>The wet court</span><span>03 / 03</span></div>', '<div class="card-meta"><span>Индонезия</span><span>03 / 03</span></div>')

# ---- 02 destination photos: Istanbul, Dubai and Bali at dusk (Unsplash) instead of the Kage stills.
# The cards keep their authored cloth/glow pipeline; the live 3D view blit is not aimed at them
# any more (no data-view), so the photo shows on every device, and the moon/lantern glows that were
# positioned for the Kage stills are dropped.
rep("url('secret-pathways-assets/generated/kage-approach.webp')", "url('secret-pathways-assets/generated/dest-istanbul.webp')")
rep("url('secret-pathways-assets/generated/kage-lantern-court.webp')", "url('secret-pathways-assets/generated/dest-dubai.webp')")
rep("url('secret-pathways-assets/generated/kage-moonwater.webp')", "url('secret-pathways-assets/generated/dest-bali.webp')")
rep('<article class="card" data-rv="up" data-view="0" data-cursor>', '<article class="card" data-rv="up" data-cursor>')
rep('<article class="card" data-rv="up" data-view="1" data-cursor>', '<article class="card" data-rv="up" data-cursor>')
rep('<article class="card" data-rv="up" data-view="2" data-cursor>', '<article class="card" data-rv="up" data-cursor>')
out = re.sub(r'\n\s*<i class="glow[^>]*></i>', '', out); count += 1

# ---- 03 advantages / tours
rep('<span class="k"><b>03</b> — Sacred Craft</span><span class="rule"></span><span class="k jp">手業</span>', '<span class="k"><b>03</b> — Преимущества</span><span class="rule"></span><span class="k jp">WHY US</span>')
rep('Five chapters. Ninety minutes. One quiet mind.', 'Индивидуально. Надёжно. По всему миру.')
rep('''Each chapter is a walk, not a lecture. You arrive at the gate, climb the
      steps, sit with the lantern, and leave with one thing worth keeping.''',
    '''Каждый маршрут мы собираем под вас: от экзотических пляжей Филиппин и Таиланда
      до древних городов Турции, Египта и Азербайджана.''')
rep('<h3>The Hidden Gate<em class="jp">山門</em></h3>', '<h3>Филиппины<em class="jp">PH</em></h3>')
rep('<p>Why a gate is a sentence, and what you agree to when you walk under one.</p>', '<p>Восхитительные пляжи, кристально чистая вода и коралловые рифы живописных островов.</p>')
rep('<span class="t">14 min</span>', '<span class="t">Тропический рай</span>')
rep('<h3>Borrowed Scenery<em class="jp">借景</em></h3>', '<h3>Вьетнам и Камбоджа<em class="jp">VN</em></h3>')
rep('<p>Shakkei: composing with a mountain you will never own.</p>', '<p>Яркие пляжи Вьетнама и древние храмы Ангкор-Вата, наполненные историей.</p>')
rep('<span class="t">18 min</span>', '<span class="t">Два в одном</span>')
rep('<h3>Charred Cypress<em class="jp">焼杉</em></h3>', '<h3>Азербайджан<em class="jp">AZ</em></h3>')
rep('<p>Yakisugi: burning a board black so the weather will let it live.</p>', '<p>Древние города, уникальная культура, местная кухня и живописные пейзажи.</p>')
rep('<span class="t">21 min</span>', '<span class="t">Кавказ</span>')
rep('<h3>Lantern Light<em class="jp">灯籠</em></h3>', '<h3>Турция<em class="jp">TR</em></h3>')
rep('<p>How a single ember decides the scale of everything around it.</p>', '<p>Эфес и Троя, пляжи Эгейского и Средиземного морей, гостеприимство и кухня.</p>')
rep('<span class="t">17 min</span>', '<span class="t">История и курорты</span>')
rep('<h3>The Vermilion Moon<em class="jp">朱月</em></h3>', '<h3>Египет<em class="jp">EG</em></h3>')
rep('<p>Why the moon burns red over the valley, and what the garden does with it.</p>', '<p>Пирамиды Гизы, храмы Луксора и курорты Красного моря для дайвинга.</p>')
rep('''<span class="t">22 min</span><i class="bar"></i>
    </div>
  </div>''', '''<span class="t">Красное море</span><i class="bar"></i>
    </div>
    <div class="les" data-les="5" data-cursor>
      <span class="k">06</span>
      <h3>Таиланд<em class="jp">TH</em></h3>
      <p>Буддийские храмы Бангкока, тайская кухня и пляжи Пхукета и Ко Самуи.</p>
      <span class="t">Острова и храмы</span><i class="bar"></i>
    </div>
  </div>''')

# ---- 04 contacts
rep('<div class="eyebrow" data-rv="fade">Chapter 04 — Afterlight</div>', '<div class="eyebrow" data-rv="fade">Глава 04 — Контакты</div>')
rep('<h2 class="display" data-rv="up">Afterlight</h2>', '<h2 class="display" data-rv="up">Контакты</h2>')
rep('''The gate does not close behind you. Take the walk whenever the noise
    gets loud — it is always the same path, and never the same light.''',
    '''Позвоните или напишите: +998 93 982 11 10, info@inwaytour.uz. Работаем с 09:00 до 18:00.
    Ташкент, ул. Паркент-2, дом 1, кв. № 17.''')
rep('<a class="cta" href="#top" data-rv="fade" data-cursor>\n    <i></i><span>Begin the walk</span>', '<a class="cta" href="tel:+998939821110" data-rv="fade" data-cursor>\n    <i></i><span>Позвонить</span>')

# ---- footer
rep('''<p>A five-chapter night walk through a Kyoto mountain temple. Three illustrated garden field notes
        sit inside a live Three.js sanctuary.</p>''', '''<p>In Way Tour — туристическая компания в Ташкенте. Индивидуальные и групповые туры,
        корпоративные поездки и тематические путешествия по всему миру.</p>''')
rep('<div><h4>Chapters</h4><ul>', '<div><h4>Разделы</h4><ul>')
rep('<li><a href="#gate" data-cursor>The Sanmon</a></li>', '<li><a href="#gate" data-cursor>О компании</a></li>')
rep('<li><a href="#pathways" data-cursor>Still Gardens</a></li>', '<li><a href="#pathways" data-cursor>Направления</a></li>')
rep('<li><a href="#lessons" data-cursor>Sacred Craft</a></li>', '<li><a href="#lessons" data-cursor>Преимущества</a></li>')
rep('<li><a href="#eternity" data-cursor>Afterlight</a></li>', '<li><a href="#eternity" data-cursor>Контакты</a></li>')
rep('<div><h4>Practice</h4><ul>', '<div><h4>Туры</h4><ul>')
rep('<li><a href="#lessons" data-cursor>Borrowed scenery</a></li>', '<li><a href="#lessons" data-cursor>Филиппины</a></li>')
rep('<li><a href="#lessons" data-cursor>Lantern light</a></li>', '<li><a href="#lessons" data-cursor>Вьетнам и Камбоджа</a></li>')
rep('<li><a href="#lessons" data-cursor>Charred cypress</a></li>', '<li><a href="#lessons" data-cursor>Турция</a></li>')
rep('<li><a href="#lessons" data-cursor>Raked gravel</a></li>', '<li><a href="#lessons" data-cursor>Египет</a></li>')
rep('<div><h4>Elsewhere</h4><ul>', '<div><h4>Связь</h4><ul>')
rep('<li><a href="#top" data-cursor>Journal</a></li>', '<li><a href="tel:+998939821110" data-cursor>+998 93 982 11 10</a></li>')
rep('<li><a href="#top" data-cursor>Field notes</a></li>', '<li><a href="mailto:info@inwaytour.uz" data-cursor>info@inwaytour.uz</a></li>')
rep('<li><a href="#top" data-cursor>Colophon</a></li>', '<li><a href="#eternity" data-cursor>Ташкент, ул. Паркент-2, 1</a></li>')
rep('<span>© 2026 Kage — Kage no Michi</span>', '<span>© 2024 In Way Tour</span>')
rep('<span class="jp">静けさは一つの技である</span>', '<span class="jp">ИНН 311374859 · МФО 00433</span>')
rep('<span>WebGL · Onest · Kyoto</span>', '<span>WebGL · Onest · Ташкент</span>')

# ---- script: rail labels, preloader jobs, 3D wordmark
rep("const names = ['The Hidden Gate', 'The Sanmon', 'Still Gardens', 'Sacred Craft', 'Afterlight', 'Colophon'];",
    "const names = ['Главная', 'О компании', 'Направления', 'Преимущества', 'Контакты', 'Подвал'];")
for old, new in [('Reading the type','Читаем шрифт'),('Pouring the ground','Заливаем землю'),('Cutting the approach','Прокладываем дорогу'),
                 ('Raising the hall','Поднимаем зал'),('Hanging the moon','Вешаем луну'),('Setting the gate','Ставим ворота'),
                 ('Placing the stones','Раскладываем камни'),('Polishing the water','Полируем воду'),('Growing the maples','Растим клёны'),
                 ('Painting the near grass','Рисуем траву'),('Raising the mist','Поднимаем туман'),('Cutting the word','Вырезаем слово')]:
    rep(f"['{old}',", f"['{new}',")
# Wordmark carries only the glyphs K A G E (+ digits); the brand word is set in the embedded Onest 700.
rep("document.fonts.load('600 320px Wordmark')", "document.fonts.load('700 320px Onest')")
rep("m.font = '600 ' + SZ + 'px Wordmark, sans-serif';", "m.font = '700 ' + SZ + 'px Onest, sans-serif';")
rep("x.font = '600 ' + SZ + 'px Wordmark, sans-serif';", "x.font = '700 ' + SZ + 'px Onest, sans-serif';")
rep("const word = 'KAGE', gl = [];", "const word = 'IN WAY', gl = [];")

# ---- typography sheet the <KageLandingPage /> frame appends (KAGE_TYPOGRAPHY.css at the configured props)
TYPO = """<style id="threeui-page-typography">
:root {
  --vermilion: #e0231c;
  --ember: #ff5a3c;
}
body { font-family: 'Onest', system-ui, -apple-system, 'Helvetica Neue', sans-serif; }
body, .body, .body-lg, .num { font-weight: 300; }
h1:not(.jp), h2:not(.jp), h3:not(.jp), .display:not(.jp) {
  font-family: 'Onest', system-ui, -apple-system, 'Helvetica Neue', sans-serif;
  font-weight: 400;
}
.display { letter-spacing: -0.012em; }
.h-hero { font-size: clamp(26px, 3.05vw, 46px); }
.h-sec { font-size: clamp(30px, 4vw, 60px); }
.body-lg { font-size: clamp(14px, 1.02vw, 17px); }
.body { font-size: 14px; }
/* In Way Tour: the .jp slots carry Latin/Cyrillic tags instead of kanji, so they use the page's own Onest. */
.jp { font-family: 'Onest', system-ui, -apple-system, 'Helvetica Neue', sans-serif; }
/* In Way Tour: the side title is eleven letters, not three kanji, so it steps aside on narrow screens. */
@media (max-width: 760px) { body[data-layout-hero="b"] .hero-side { display: none; } }
</style>
</head>"""
rep('</head>', TYPO)

open('index.html', 'w', encoding='utf-8').write(out)
print(f'index.html written, {count} replacements, {len(out)} bytes')
