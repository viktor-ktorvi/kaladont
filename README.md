# Kaladont

[Kaladont](https://en.wikipedia.org/wiki/Kaladont) is a word chain game popular amongst kids in Serbo-croatian speaking regions, where players take turns saying words, each starting with the last two letters of the previous one — for example, *tantalum* → *umpire* → *rerun* → *unpleasant*. The game's name comes from the Austrian toothpaste brand Kalodont, which became the canonical winning word because no South Slavic word begins with "nt". This project simulates the game across multiple languages using lemmatized word lists from [kaikki.org](https://kaikki.org) Wiktionary data, running Monte Carlo experiments to measure how long chains can get.

## Installation

```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
```

## Usage

Play a single language (Monte Carlo simulation):

```shell
uv run python -m scripts.kaladont --language en --simulations 100
```

Benchmark all languages and export results:

```shell
uv run python -m scripts.benchmark --simulations 1000 --output results.csv
```

## Supported languages

Game length statistics from 1000 simulations, sorted by mean chain length:

| Language | Min Freq | Min Len | Overlap | Words | Max | Mean | Median | Example chain |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Serbo-Croatian (Latin) | — | 3 | 2       | 26,902 | 291 | 51.2 | 39.0 | kovrča → čakšire → reparacija → jao → aorist → stoprem → emocija → jal → alt |
| Indonesian | — | 3 | 2       | 20,347 | 269 | 43.8 | 37.0 | swaguna → narkose → sensorik → ikonoklas → astronaut → uterus → usung → ngocokin → inokulasi → silt |
| Serbo-Croatian (Cyrillic) | — | 3 | 2       | 23,233 | 201 | 36.6 | 27.0 | омладина → назнака → кадаиф |
| Georgian | — | 3 | 2       | 16,905 | 192 | 35.7 | 26.0 | ხოხისმიერად → ადამიანებისადმი → მიწათმოქმედება → ბანაობს |
| Malay | — | 3 | 2       | 6,862 | 118 | 33.2 | 30.0 | sekretaris → isteri → rilek → ekor → original → alamak → aksesori → ritu → tumbuh |
| Italian | 2.0 | 3 | 2       | 33,191 | 145 | 25.3 | 18.0 | agonistico → controverso → solferino → nocca → carreggiata → tabù |
| Korean | — | 2 | 1       | 27,140 | 164 | 24.9 | 18.0 | 신소젖 → 젖꼭지 → 지휘관 → 관절 → 절이다 → 다섯 |
| Finnish | 2.0 | 3 | 2       | 34,066 | 183 | 24.6 | 18.0 | kyynisyys → ystävyys → ystävällisesti → tietoisku → kumea |
| Persian | — | 3 | 2       | 10,557 | 117 | 24.3 | 19.5 | هراتی → تیمچه → چهارده → دهقانی → نیست → ستیزه → زهرشناسی → سیاهه |
| Romanian | — | 3 | 2       | 68,983 | 173 | 20.8 | 15.0 | beseadă → dărâmare → readmonesta → talpă → păsuială → lătrător → oricalc |
| Macedonian | — | 3 | 2       | 37,883 | 213 | 19.5 | 13.0 | развлажува → ваја → јачменов → овенчува → вашингтонец |
| Lithuanian | — | 3 | 2       | 6,342 | 55 | 16.7 | 14.0 | aptikti → tirpti → tiesioginis → islamas → astrofizika → kaboti → tirant |
| Swahili | — | 3 | 2       | 7,761 | 71 | 12.9 | 9.0 | kifa → fariji → jiostratejia |
| Spanish | 2.0 | 3 | 2       | 28,595 | 63 | 12.8 | 11.0 | tico → cohesionar → arriano → notificación → ónix → ixil → iluminar → arrabal → almunia |
| Turkish | — | 3 | 2       | 16,959 | 89 | 12.6 | 9.0 | bencil → ilköğretim → imsakiye → yerküre → reze → zevç |
| Portuguese | 2.0 | 3 | 2       | 23,067 | 54 | 8.2 | 6.0 | ensejo → joãozinho → horizontalmente → tempura → raquete → telescópio → ionização |
| Arabic | — | 3 | 2       | 46,904 | 39 | 6.4 | 5.0 | مضين → ينحملن → لنا → نافورة |
| English | 2.0 | 3 | 2       | 41,022 | 32 | 5.2 | 4.0 | prenuptial → alchemist → streaming |
| Czech | 2.0 | 3 | 2       | 20,578 | 24 | 5.1 | 4.0 | posadit → italský → kýč |
| Albanian | — | 3 | 2       | 9,406 | 42 | 4.6 | 3.0 | shtat → ato → torrë → rërët |
| Dutch | 2.0 | 3 | 2       | 25,575 | 22 | 4.3 | 3.0 | proteïne → neurowetenschapper → erfstuk |
| Swedish | 2.0 | 3 | 2       | 24,340 | 27 | 4.2 | 3.0 | tajma → maktlös → östtyska → kantarell |
| Bulgarian | — | 3 | 2       | 14,283 | 24 | 4.0 | 3.0 | балерина → надвес → есен → енергично → нормален → ендшпил → илюзионизъм |
| French | 2.0 | 3 | 2       | 27,105 | 22 | 4.0 | 3.0 | initiale → leurrer → errance → centième → menu → nul → ultramoderne → neurochirurgien → enluminure → reconstituant |
| German | 2.0 | 3 | 2       | 39,209 | 24 | 3.9 | 3.0 | Strukturwandel → elektrisch → chillen → entbehrlich → charismatisch → checken → enttäuschend |
| Russian | 2.0 | 3 | 2       | 27,855 | 20 | 3.6 | 3.0 | доминировать → тьма → мания |
| Ukrainian | — | 3 | 2       | 22,940 | 17 | 3.4 | 3.0 | ригати → тиква → ваш |
| Polish | 2.0 | 3 | 2       | 21,609 | 24 | 3.3 | 2.0 | miano → nowożytny → nylon → onieśmielony → nyt |
| Armenian | — | 3 | 2       | 13,516 | 20 | 3.1 | 2.0 | հրապարակ → ակրոպոլիս → իսլանդերեն → ենթադրյալ → ալեհեր → երկյուղ |
| Slovak | — | 3 | 2       | 7,025 | 18 | 3.0 | 2.0 | slovníkový → výškar → architekt → ktosi → siedmy → mytológia |
| Hindi | — | 3 | 2       | 15,995 | 13 | 2.3 | 2.0 | गुणसूत्रबिंदु → दुख़्तर → तरक़्क़ी |
| Latvian | — | 3 | 2       | 13,915 | 11 | 2.2 | 2.0 | cieši → šie → iezaļš |
| Greek | — | 3 | 2       | 24,284 | 9 | 2.1 | 2.0 | ράγισμα → μαόνι → νικοτίνη → νηπιαγωγός |






Word lists are sourced from [kaikki.org](https://kaikki.org/dictionary/) (English Wiktionary, lemmatized). Frequency filtering uses [wordfreq](https://github.com/rspeer/wordfreq) Zipf scores where corpus coverage is sufficient.

### Options

| Flag | Short | Default | Description |
| --- | --- | --- | --- |
| `--language` | `-l` | `sh-latin` | Language to play |
| `--simulations` | `-n` | `100` | Number of Monte Carlo simulations |
| `--min-frequency` | `-f` | per-language | Minimum Zipf frequency (0 = disabled) |
| `--min-word-size` | `-w` | `3` | Minimum word length in characters |

### Word lists

Word lists are downloaded from [kaikki.org](https://kaikki.org/dictionary/), which parses the English Wiktionary into structured JSONL. Wiktionary entries are generally dictionary headwords (lemmas), though it also contains entries for individual inflected forms that redirect to the base word.

The raw data is filtered down to playable words by removing:
- **Proper nouns, affixes, symbols** — excluded by part-of-speech tag
- **Multi-word entries and hyphens** — only single tokens allowed
- **Inflected and alternative forms** — entries tagged as `form-of` or `alt-of` in any sense are excluded
- **Abbreviations** — all-caps words (e.g. `NATO`, `DNA`) and entries tagged as abbreviations or initialisms
- **Words without a vowel** — catches lowercase abbreviations like `src`, `rsvp` (Latin script only)
- **Proper-noun casing** — words starting with a capital are dropped, except in languages where common nouns are capitalised (e.g. German)
- **Low-frequency words** — for languages with large, well-covered corpora (English, Spanish, French, German, etc.) a [wordfreq](https://github.com/rspeer/wordfreq) Zipf score threshold of 2.0 is applied to filter out rare technical and medical terms; smaller or less-covered languages skip this step to avoid over-filtering

Despite this, **the word lists are imperfect** — obscure loanwords, archaic forms, highly technical terms, and inflected forms can still slip through, either because they appear as legitimate Wiktionary headwords or due to inconsistent tagging, but so do legitimate words get filtered out. The simulation treats all surviving words as equally valid.

The table below shows a random sample of surviving and filtered-out words per language, giving a sense of what passes through and what gets removed:

<!-- BEGIN:word-samples -->
<table>
<tr><th>Language</th><th>Surviving words</th><th>Filtered out words</th></tr>
<tr><td>Serbo-Croatian (Latin)</td><td><em>povučen</em>, <em>ražanj</em>, <em>medicina</em>, <em>paleozoik</em>, <em>razveseliti</em>, <em>raskid</em>, <em>autonomist</em>, <em>cinabarit</em>, <em>krpariti</em>, <em>vegetarijanizam</em>, <em>peteljka</em>, <em>delinkvent</em>, <em>odmicati</em>, <em>orman</em>, <em>krvni</em>, <em>istinit</em>, <em>vagon</em>, <em>morski</em>, <em>fursat</em>, <em>cenzus</em>, <em>direktno</em>, <em>ljuljaška</em>, <em>slinav</em>, <em>rečnik</em>, <em>naočit</em></td><td><em>Januš</em>, <em>majstorom</em>, <em>ploči</em>, <em>Dretar</em>, <em>klena</em>, <em>proleteri svih zemalja, ujedinite se</em>, <em>tkano</em>, <em>potezi</em>, <em>radnje</em>, <em>čvarci</em>, <em>Helsinki</em>, <em>radarima</em>, <em>donesti</em>, <em>Zadro</em>, <em>kolenu</em>, <em>Bogumil</em>, <em>Cetinjanin</em>, <em>smeten</em>, <em>dece</em>, <em>krikom</em>, <em>Vodomir</em>, <em>Booleova logika</em>, <em>glasba</em>, <em>bulom</em>, <em>tamo-amo</em></td></tr>
<tr><td>Serbo-Croatian (Cyrillic)</td><td><em>засебно</em>, <em>секта</em>, <em>хумореска</em>, <em>задржати</em>, <em>цинк</em>, <em>дарвинизам</em>, <em>поправак</em>, <em>елизија</em>, <em>спречавати</em>, <em>пакет</em>, <em>посекотина</em>, <em>картица</em>, <em>котловина</em>, <em>зачахурити</em>, <em>судионик</em>, <em>плеснивост</em>, <em>чинити</em>, <em>окречити</em>, <em>фестивал</em>, <em>изрека</em>, <em>сукладно</em>, <em>ненормалан</em>, <em>индонезијски</em>, <em>звијезда</em>, <em>хумано</em></td><td><em>Тихи океан</em>, <em>гњусан</em>, <em>одмаћи</em>, <em>забугаривати</em>, <em>Новозеланђанка</em>, <em>-ушина</em>, <em>Египћанин</em>, <em>-ава</em>, <em>-це</em>, <em>Индонежанин</em>, <em>Социјалистичка Република Србија</em>, <em>лиже</em>, <em>Валпово</em>, <em>Бјеловар</em>, <em>Швабо</em>, <em>Волга</em>, <em>носовима</em>, <em>Витомир</em>, <em>добивати</em>, <em>лисицу</em>, <em>доодила</em>, <em>Еквадорац</em>, <em>носић</em>, <em>Ковачићи</em>, <em>ћер</em></td></tr>
<tr><td>Macedonian</td><td><em>повеќенасочен</em>, <em>енисејски</em>, <em>осети</em>, <em>некоректност</em>, <em>симпатичност</em>, <em>мокасина</em>, <em>лондонец</em>, <em>позитивност</em>, <em>њуделхиец</em>, <em>синовски</em>, <em>методолошки</em>, <em>купечки</em>, <em>конопот</em>, <em>рола</em>, <em>болежлив</em>, <em>незамајан</em>, <em>фер</em>, <em>недијагнозирање</em>, <em>домаќин</em>, <em>недоловлив</em>, <em>бездомник</em>, <em>модератор</em>, <em>докуп</em>, <em>феноменолошки</em>, <em>деминутивен</em></td><td><em>дваесет и осуммина</em>, <em>фати на дело</em>, <em>подзамрзнат</em>, <em>во кратки црти</em>, <em>преименуван</em>, <em>однесен</em>, <em>формализирање</em>, <em>аман заман</em>, <em>Водопост</em>, <em>проституирање</em>, <em>линии</em>, <em>понадворешен</em>, <em>славеи</em>, <em>кметици</em>, <em>сакало</em>, <em>Дака</em>, <em>напојници</em>, <em>раце</em>, <em>Егеју</em>, <em>помножување</em>, <em>извишен</em>, <em>школки</em>, <em>лека ноќ</em>, <em>расчовечен</em>, <em>позабавуван</em></td></tr>
<tr><td>Bulgarian</td><td><em>бръснарница</em>, <em>рицар</em>, <em>каузативен</em>, <em>препрочета</em>, <em>чорбаджия</em>, <em>жигосвам</em>, <em>век</em>, <em>избягване</em>, <em>хлас</em>, <em>бол</em>, <em>поледица</em>, <em>боря</em>, <em>брощ</em>, <em>даващия</em>, <em>илач</em>, <em>тетрев</em>, <em>седелия</em>, <em>физика</em>, <em>корения</em>, <em>ажиотаж</em>, <em>рай</em>, <em>питач</em>, <em>минута</em>, <em>книжовност</em>, <em>кривак</em></td><td><em>опираме</em>, <em>светлината</em>, <em>изпят</em>, <em>начала</em>, <em>домитали</em>, <em>подвеждалата</em>, <em>авангарда</em>, <em>корящите</em>, <em>захапвах</em>, <em>решете</em>, <em>изгребвахме</em>, <em>ендемична</em>, <em>електрически заряд</em>, <em>Плутон</em>, <em>травматичните</em>, <em>почитаха</em>, <em>прегръщаха</em>, <em>агротехничка</em>, <em>допринасяш</em>, <em>пърдяхте</em>, <em>поизмела</em>, <em>насичал</em>, <em>спрелите</em>, <em>наследяваното</em>, <em>Дамгов</em></td></tr>
<tr><td>Russian</td><td><em>двойной</em>, <em>рой</em>, <em>ливанский</em>, <em>хлопнуть</em>, <em>вымолить</em>, <em>якорь</em>, <em>магистратура</em>, <em>получеловек</em>, <em>работоспособный</em>, <em>геофизик</em>, <em>лор</em>, <em>джинсовый</em>, <em>пукать</em>, <em>браунинг</em>, <em>горняк</em>, <em>северокорейский</em>, <em>загорелый</em>, <em>перерасти</em>, <em>истинность</em>, <em>мяч</em>, <em>товарный</em>, <em>католичество</em>, <em>интим</em>, <em>обвязать</em>, <em>агрономия</em></td><td><em>первопроходчиками</em>, <em>викторинах</em>, <em>вываливаемся</em>, <em>трунить</em>, <em>изворачивались</em>, <em>фарватерам</em>, <em>осветитесь</em>, <em>поджидающий</em>, <em>подвернул</em>, <em>отринул</em>, <em>этикеткою</em>, <em>опросу</em>, <em>чокнулся</em>, <em>маоизмом</em>, <em>Артемида</em>, <em>набатов</em>, <em>кровавимый</em>, <em>отвращением</em>, <em>нардепе</em>, <em>штрафам</em>, <em>лор</em>, <em>продаст</em>, <em>ведьмаками</em>, <em>подпоркам</em>, <em>заморозили</em></td></tr>
<tr><td>Ukrainian</td><td><em>ієрархічний</em>, <em>низина</em>, <em>палець</em>, <em>вимусити</em>, <em>мотати</em>, <em>натякати</em>, <em>мінімум</em>, <em>хвора</em>, <em>намотувати</em>, <em>ототожнити</em>, <em>геоморфологічний</em>, <em>авдит</em>, <em>топка</em>, <em>потовстіти</em>, <em>барель</em>, <em>совкодрочер</em>, <em>загальновідомий</em>, <em>вілла</em>, <em>афроамериканець</em>, <em>пароплав</em>, <em>акваріум</em>, <em>модно</em>, <em>розвантажувати</em>, <em>верблюжа</em>, <em>виходити</em></td><td><em>івано-франківський</em>, <em>Герца</em>, <em>Бухарестові</em>, <em>нижче</em>, <em>сумнівавсь</em>, <em>Сінгапур</em>, <em>насиченій</em>, <em>їхнім</em>, <em>чітких</em>, <em>родам</em>, <em>красива</em>, <em>вимив</em>, <em>сяде</em>, <em>мікро-</em>, <em>актів</em>, <em>тверкінгом</em>, <em>столиками</em>, <em>запозичення</em>, <em>бонусами</em>, <em>-янка</em>, <em>лексиконів</em>, <em>окупанти</em>, <em>дисплеях</em>, <em>Георгійович</em>, <em>щокам</em></td></tr>
<tr><td>Polish</td><td><em>siłownia</em>, <em>przeprowadzić</em>, <em>aplikacja</em>, <em>biskup</em>, <em>ilekroć</em>, <em>upolować</em>, <em>odwaga</em>, <em>kulturystyka</em>, <em>gwizdka</em>, <em>kryminał</em>, <em>ton</em>, <em>poprzedzać</em>, <em>rodzinny</em>, <em>balans</em>, <em>hałaśliwy</em>, <em>odpychać</em>, <em>kadra</em>, <em>petycja</em>, <em>pozbawiać</em>, <em>wiek</em>, <em>defetyzm</em>, <em>upór</em>, <em>cool</em>, <em>krocz</em>, <em>zestawić</em></td><td><em>klimaksie</em>, <em>zarchiwizowany</em>, <em>rewerans</em>, <em>Seksty</em>, <em>klapką</em>, <em>Rzeszót</em>, <em>Plaskiewicz</em>, <em>zawziętszy</em>, <em>pijam</em>, <em>refowałby</em>, <em>słonczy</em>, <em>abonował</em>, <em>pomylenie</em>, <em>wynajmujmy</em>, <em>przyprawiałbym</em>, <em>decymuję</em>, <em>neuronowym</em>, <em>kompanować</em>, <em>Dębowy</em>, <em>obserwowaliśmy</em>, <em>pychotą</em>, <em>kremacjami</em>, <em>Wawrosz</em>, <em>odraczałyście</em>, <em>wypędzało</em></td></tr>
<tr><td>Czech</td><td><em>sponzor</em>, <em>stezka</em>, <em>akupunktura</em>, <em>pootočit</em>, <em>mělčina</em>, <em>okolky</em>, <em>vychovaný</em>, <em>javor</em>, <em>pojíst</em>, <em>vykřičník</em>, <em>pach</em>, <em>spodnička</em>, <em>nalezený</em>, <em>naživu</em>, <em>parmezán</em>, <em>součin</em>, <em>záměrně</em>, <em>podpořit</em>, <em>čtivý</em>, <em>scénárista</em>, <em>dvouletý</em>, <em>balón</em>, <em>průsečík</em>, <em>kvóta</em>, <em>výřečný</em></td><td><em>polit</em>, <em>sila</em>, <em>prudil</em>, <em>bažantů</em>, <em>Štikarovský</em>, <em>pedantický</em>, <em>falešné dilema</em>, <em>Gryc</em>, <em>Frídin</em>, <em>děde</em>, <em>Nymburk</em>, <em>stolek</em>, <em>tahán</em>, <em>mám</em>, <em>jakutština</em>, <em>tvore</em>, <em>bezstarostněji</em>, <em>extraartikulární</em>, <em>strukturovatelný</em>, <em>Mrhač</em>, <em>oblékni</em>, <em>podle mě</em>, <em>Hosák</em>, <em>sestry</em>, <em>Lodín</em></td></tr>
<tr><td>Slovak</td><td><em>ununtrium</em>, <em>stromový</em>, <em>manažér</em>, <em>antropomorfický</em>, <em>automobilový</em>, <em>plynojem</em>, <em>pozor</em>, <em>jaspis</em>, <em>okrajový</em>, <em>drak</em>, <em>panteizmus</em>, <em>výťahový</em>, <em>antiamerikanizmus</em>, <em>bronzový</em>, <em>turizmus</em>, <em>vidieť</em>, <em>sadový</em>, <em>basista</em>, <em>biatlonový</em>, <em>obdobie</em>, <em>sadra</em>, <em>afarčina</em>, <em>gastrológia</em>, <em>vyjsť</em>, <em>medvedica</em></td><td><em>hundrete</em>, <em>sokolica</em>, <em>lakťu</em>, <em>Arno</em>, <em>kane</em>, <em>hrče</em>, <em>Bodrog</em>, <em>vlnka</em>, <em>buku</em>, <em>Pucher</em>, <em>Elvíra</em>, <em>Tamilnádu</em>, <em>vdovách</em>, <em>vodičský preukaz</em>, <em>chudá</em>, <em>kňazík</em>, <em>luhala</em>, <em>Sokrates</em>, <em>najvyšší</em>, <em>sople</em>, <em>hôľ</em>, <em>dcérkach</em>, <em>Geier</em>, <em>najbohatší</em>, <em>predstavovať</em></td></tr>
<tr><td>Lithuanian</td><td><em>sportinis</em>, <em>kadangi</em>, <em>atlaikas</em>, <em>įdavėjas</em>, <em>interesas</em>, <em>dubnis</em>, <em>diegti</em>, <em>valsas</em>, <em>paleontologija</em>, <em>randant</em>, <em>tamsiaakis</em>, <em>nurengsiant</em>, <em>dovanoti</em>, <em>išbučiuoti</em>, <em>karpa</em>, <em>prašom</em>, <em>buksyras</em>, <em>ryžis</em>, <em>kudakuoti</em>, <em>atsistebėti</em>, <em>žvaigždiškas</em>, <em>patarti</em>, <em>pusdievis</em>, <em>skundas</em>, <em>risti</em></td><td><em>sapnavusioje</em>, <em>airiškuose</em>, <em>stebinčiajam</em>, <em>oksidai</em>, <em>įspūdingiausioms</em>, <em>mylėjusiai</em>, <em>blogiausiąsias</em>, <em>būdavusiai</em>, <em>teatidaro</em>, <em>paradoksams</em>, <em>bendravai</em>, <em>mažiausiosiose</em>, <em>meniškesniesiems</em>, <em>ištylėtumėme</em>, <em>bėgusių</em>, <em>lenkiškuose</em>, <em>pisančioms</em>, <em>mažesniąją</em>, <em>audros</em>, <em>palieka</em>, <em>įduosiančiose</em>, <em>išvalgantis</em>, <em>gnostiškam</em>, <em>ejakuliavusias</em>, <em>erekcijai</em></td></tr>
<tr><td>Latvian</td><td><em>skuveklis</em>, <em>raudādams</em>, <em>ķeizariski</em>, <em>izskatīties</em>, <em>tadžikiski</em>, <em>erchercogiste</em>, <em>necepšana</em>, <em>atriebjošs</em>, <em>nemeklēts</em>, <em>apavniece</em>, <em>mats</em>, <em>garš</em>, <em>neizardams</em>, <em>spēkone</em>, <em>mundrāk</em>, <em>nepaarušais</em>, <em>purpurs</em>, <em>francijs</em>, <em>nevingrodams</em>, <em>centrāle</em>, <em>dabūjams</em>, <em>nepārcepušais</em>, <em>locīt</em>, <em>kurināts</em>, <em>korejietis</em></td><td><em>neadāmiem</em>, <em>visērtākos</em>, <em>kosmiskākus</em>, <em>Bāzeles</em>, <em>producējušus</em>, <em>ūdeņainajām</em>, <em>uzaramu</em>, <em>miglās</em>, <em>nedegošos</em>, <em>neredzējušam</em>, <em>Anna</em>, <em>neautajai</em>, <em>spriedošas</em>, <em>centralizējošajām</em>, <em>tālākajam</em>, <em>simbolistiskā</em>, <em>sistos</em>, <em>ģeometriskākajās</em>, <em>stingākie</em>, <em>īgnākajai</em>, <em>saprastu</em>, <em>sargāmie</em>, <em>reģistrā</em>, <em>modrībā</em>, <em>nenoteicošiem</em></td></tr>
<tr><td>German</td><td><em>Weinbau</em>, <em>Ernährung</em>, <em>Ausprägung</em>, <em>Thematik</em>, <em>Küchengerät</em>, <em>parteilos</em>, <em>Zurückschreiben</em>, <em>Tweed</em>, <em>Hochdruck</em>, <em>Stubenarrest</em>, <em>Funktionalismus</em>, <em>Jungsteinzeit</em>, <em>windstill</em>, <em>Heimcomputer</em>, <em>Nomenklatur</em>, <em>abgraben</em>, <em>tiefschwarz</em>, <em>Kreuzweg</em>, <em>Aufenthaltsraum</em>, <em>global</em>, <em>Umwelttechnik</em>, <em>Programmiererin</em>, <em>untätig</em>, <em>docken</em>, <em>Geschichtsrevisionismus</em></td><td><em>Hansa</em>, <em>Abschnittsende</em>, <em>Handballspielers</em>, <em>Brennholze</em>, <em>übertriffst</em>, <em>spickten</em>, <em>Zivilverteidigungen</em>, <em>osmotische</em>, <em>untergehest</em>, <em>Parfum</em>, <em>unterschiebst</em>, <em>einunddreißigstes</em>, <em>desavouierte</em>, <em>sportlicheren</em>, <em>Knochenfischen</em>, <em>hellwacher</em>, <em>überschattest</em>, <em>regulärerer</em>, <em>Quotienten</em>, <em>traumatisierst</em>, <em>zirconiumhaltigsten</em>, <em>herzog</em>, <em>tapezierte</em>, <em>Küchenlöffels</em>, <em>tablettenförmig</em></td></tr>
<tr><td>English</td><td><em>methoxy</em>, <em>purification</em>, <em>prebendary</em>, <em>activewear</em>, <em>mealy</em>, <em>viscount</em>, <em>concert</em>, <em>currently</em>, <em>prion</em>, <em>imperishable</em>, <em>postmaster</em>, <em>wetland</em>, <em>persecutor</em>, <em>jolting</em>, <em>vier</em>, <em>tassie</em>, <em>upstate</em>, <em>stocking</em>, <em>fanaticism</em>, <em>wry</em>, <em>tuned</em>, <em>earpiece</em>, <em>awardee</em>, <em>slimline</em>, <em>behaved</em></td><td><em>haploidify</em>, <em>Harry Holts</em>, <em>elaenias</em>, <em>dutifullness</em>, <em>antireproductive</em>, <em>wingwalkers</em>, <em>centralisms</em>, <em>Heeze-Leende</em>, <em>plated up</em>, <em>Doue</em>, <em>gingerbready</em>, <em>sibilates</em>, <em>seismomicrophone</em>, <em>radlib</em>, <em>tabtop</em>, <em>muroid</em>, <em>pediatrists</em>, <em>Z-plasty</em>, <em>advertainment</em>, <em>heck no</em>, <em>Yellow Dog</em>, <em>petrogenetically</em>, <em>Ingalls</em>, <em>khomoks</em>, <em>candle-wick</em></td></tr>
<tr><td>Dutch</td><td><em>rollen</em>, <em>nep</em>, <em>bezorgen</em>, <em>kogel</em>, <em>rijksdag</em>, <em>kaften</em>, <em>concurrentie</em>, <em>gijzelnemer</em>, <em>recentelijk</em>, <em>karma</em>, <em>meevallen</em>, <em>scheepswerf</em>, <em>opstanding</em>, <em>vuilnisbelt</em>, <em>travestiet</em>, <em>frituurpan</em>, <em>container</em>, <em>bezetten</em>, <em>gentherapie</em>, <em>admiraal</em>, <em>onwrikbaar</em>, <em>aanstekelijk</em>, <em>ondoorgrondelijk</em>, <em>drie</em>, <em>alleskunner</em></td><td><em>galjoot</em>, <em>benamen</em>, <em>oogappels</em>, <em>Afar</em>, <em>onstuimigs</em>, <em>luchtziek</em>, <em>Exloo</em>, <em>bezettertjes</em>, <em>weigeraar</em>, <em>treurduif</em>, <em>terminologietje</em>, <em>dodenakkertje</em>, <em>Holterbroek</em>, <em>Kuikseind</em>, <em>suikerbrood</em>, <em>lhbt</em>, <em>beekjuffer</em>, <em>jeukte</em>, <em>zadelkleed</em>, <em>huilebalkt</em>, <em>poserend</em>, <em>alkjes</em>, <em>ontvlechtingen</em>, <em>disputen</em>, <em>aanknopingspuntjes</em></td></tr>
<tr><td>Swedish</td><td><em>krock</em>, <em>samexistens</em>, <em>blomblad</em>, <em>mörkhyad</em>, <em>oförståelse</em>, <em>röst</em>, <em>härförare</em>, <em>psykologi</em>, <em>sexualdrift</em>, <em>nybäddad</em>, <em>program</em>, <em>groll</em>, <em>aptitretare</em>, <em>förnärmad</em>, <em>kärnenergi</em>, <em>diet</em>, <em>spela</em>, <em>sammanstötning</em>, <em>kalasjnikov</em>, <em>lider</em>, <em>förlika</em>, <em>räcka</em>, <em>fjärde</em>, <em>stabilisera</em>, <em>poppel</em></td><td><em>tillmätts</em>, <em>gruppspels</em>, <em>kulturfenomenet</em>, <em>samlevnadens</em>, <em>bruksföremålen</em>, <em>inkarnera</em>, <em>krullhårig</em>, <em>tebrickorna</em>, <em>konstgjorda</em>, <em>förordnar</em>, <em>rwandiskan</em>, <em>pyntet</em>, <em>essentialister</em>, <em>skavnings</em>, <em>urtavlans</em>, <em>anlitade</em>, <em>framgår</em>, <em>vassen</em>, <em>parallellsamhällets</em>, <em>finansmans</em>, <em>isoton</em>, <em>persikoträdets</em>, <em>knaprat</em>, <em>stolpillren</em>, <em>motsägelselust</em></td></tr>
<tr><td>Spanish</td><td><em>rejuvenecimiento</em>, <em>chucha</em>, <em>afligido</em>, <em>apalear</em>, <em>topar</em>, <em>mezcolanza</em>, <em>relajar</em>, <em>artrosis</em>, <em>persecución</em>, <em>pierna</em>, <em>lagar</em>, <em>itálica</em>, <em>desgobierno</em>, <em>bronceador</em>, <em>dinero</em>, <em>despavorido</em>, <em>carbonera</em>, <em>también</em>, <em>venoso</em>, <em>cachorro</em>, <em>referendo</em>, <em>lago</em>, <em>reescribir</em>, <em>bobada</em>, <em>reencuentro</em></td><td><em>dantos</em>, <em>celebrándolos</em>, <em>afligiere</em>, <em>moderaría</em>, <em>nebulizaras</em>, <em>a cielo abierto</em>, <em>desalmacenarías</em>, <em>hierosolimitano</em>, <em>gonadal</em>, <em>twerkeasen</em>, <em>barroquismas</em>, <em>reorquestaron</em>, <em>deslastrándoles</em>, <em>alcanzaría</em>, <em>desmoralizarles</em>, <em>difaman</em>, <em>desnacemos</em>, <em>embrear</em>, <em>desliares</em>, <em>aguisé</em>, <em>patrimonializaréis</em>, <em>pintarais</em>, <em>prototiparan</em>, <em>parceros</em>, <em>climatólogos</em></td></tr>
<tr><td>French</td><td><em>pigeon</em>, <em>digérer</em>, <em>cupidon</em>, <em>auvent</em>, <em>relocation</em>, <em>alimentaire</em>, <em>provoquer</em>, <em>chlorophylle</em>, <em>processeur</em>, <em>écriteau</em>, <em>antiviral</em>, <em>dynastie</em>, <em>horticulture</em>, <em>méridienne</em>, <em>accablant</em>, <em>mutualiser</em>, <em>traque</em>, <em>diffamer</em>, <em>keynésianisme</em>, <em>séculier</em>, <em>muséographique</em>, <em>indemnisation</em>, <em>renouvellement</em>, <em>carnassier</em>, <em>brésil</em></td><td><em>retestèrent</em>, <em>manivelles</em>, <em>édenterait</em>, <em>encombreraient</em>, <em>photocopias</em>, <em>clopinerions</em>, <em>stomodæum</em>, <em>conspuons</em>, <em>célèbrerez</em>, <em>préréglera</em>, <em>époptique</em>, <em>suburbicaire</em>, <em>engloberez</em>, <em>enlacerait</em>, <em>locution nominale</em>, <em>prévaudrai</em>, <em>crachotât</em>, <em>mastiquons</em>, <em>oevrée</em>, <em>crècherons</em>, <em>transsexuels</em>, <em>ROU</em>, <em>avachiront</em>, <em>resaccadait</em>, <em>bastiaise</em></td></tr>
<tr><td>Italian</td><td><em>esclamazione</em>, <em>trench</em>, <em>avvicinamento</em>, <em>giovane</em>, <em>disertore</em>, <em>scorno</em>, <em>interbase</em>, <em>ventrale</em>, <em>annullabile</em>, <em>piccardo</em>, <em>crono</em>, <em>loro</em>, <em>sentimento</em>, <em>staccionata</em>, <em>prospiciente</em>, <em>tridimensionale</em>, <em>gongola</em>, <em>domandarci</em>, <em>trifoglio</em>, <em>autostazione</em>, <em>marinaro</em>, <em>restio</em>, <em>possessione</em>, <em>trovane</em>, <em>lesbismo</em></td><td><em>svettiate</em>, <em>polifagi</em>, <em>sgorbiata</em>, <em>preannunciati</em>, <em>tortureremmo</em>, <em>bellicosa</em>, <em>cofondarono</em>, <em>puzzeremmo</em>, <em>scalogna</em>, <em>foranea</em>, <em>bivaccherebbero</em>, <em>vagillare</em>, <em>avvantaggiarvene</em>, <em>flagrano</em>, <em>sbagliandole</em>, <em>guarnii</em>, <em>accreditarsi</em>, <em>riappacificandoci</em>, <em>indignarvi</em>, <em>compartimentalizzavano</em>, <em>volteggiaste</em>, <em>radiocomandarono</em>, <em>vibrerebbero</em>, <em>ridarvi</em>, <em>candissi</em></td></tr>
<tr><td>Portuguese</td><td><em>zoologia</em>, <em>dono</em>, <em>bafafá</em>, <em>distraído</em>, <em>luís</em>, <em>devorar</em>, <em>redecorar</em>, <em>sucessor</em>, <em>vanguardista</em>, <em>croissant</em>, <em>esnobe</em>, <em>incongruente</em>, <em>demolição</em>, <em>gémeo</em>, <em>passageiro</em>, <em>líquen</em>, <em>recentemente</em>, <em>meu</em>, <em>sinestesia</em>, <em>falecer</em>, <em>cintura</em>, <em>nadar</em>, <em>humilhante</em>, <em>tampo</em>, <em>rapa</em></td><td><em>alçapremáramos</em>, <em>fretasses</em>, <em>rejubilais</em>, <em>mordi</em>, <em>endereçariam</em>, <em>contagiada</em>, <em>bembé</em>, <em>semelhou</em>, <em>intimidemos</em>, <em>infirmeis</em>, <em>exterminassem</em>, <em>pufes</em>, <em>pastoreásseis</em>, <em>desencanaremos</em>, <em>compactávamos</em>, <em>enrustiu</em>, <em>desenvolvia</em>, <em>atturarmos</em>, <em>faz tudo</em>, <em>rotastes</em>, <em>procrastinarão</em>, <em>esbraseáramos</em>, <em>bobeássemos</em>, <em>acetificarão</em>, <em>pintalgaríeis</em></td></tr>
<tr><td>Romanian</td><td><em>masturbarăm</em>, <em>bitum</em>, <em>jnepeniș</em>, <em>partițiune</em>, <em>conexare</em>, <em>satirizare</em>, <em>pergamentos</em>, <em>electrocorticografie</em>, <em>aligote</em>, <em>incuba</em>, <em>alodial</em>, <em>augment</em>, <em>vinotecă</em>, <em>bandajat</em>, <em>ișala</em>, <em>geometrizat</em>, <em>fierbinte</em>, <em>geognozie</em>, <em>vindecabil</em>, <em>strabic</em>, <em>triorhidie</em>, <em>trabuc</em>, <em>codaj</em>, <em>adiționare</em>, <em>urocultură</em></td><td><em>Petcuță</em>, <em>suplicat</em>, <em>Cotorbești</em>, <em>asemene</em>, <em>high-life</em>, <em>deget mijlociu</em>, <em>ioanită</em>, <em>des-de-noapte</em>, <em>pensiuni</em>, <em>funcționați</em>, <em>sodomizează</em>, <em>aburit</em>, <em>cataloage</em>, <em>Moigrad-Porolissum</em>, <em>lovitură de pedeapsă</em>, <em>pliroforițiune</em>, <em>tărăgănat</em>, <em>proglot</em>, <em>Valea Fetei</em>, <em>Mâner</em>, <em>greva</em>, <em>Nădăștean</em>, <em>moalele capului</em>, <em>Pătrășcani</em>, <em>bâjbâit</em></td></tr>
<tr><td>Greek</td><td><em>γεωδαιτικός</em>, <em>κλάδα</em>, <em>επιγράφομαι</em>, <em>αντίρροπος</em>, <em>ανεξαργύρωτος</em>, <em>αναγνωρισμένος</em>, <em>αργομισθία</em>, <em>αποφαντικός</em>, <em>αστέρι</em>, <em>αμπελουργική</em>, <em>διένεξη</em>, <em>τζιτζίκι</em>, <em>προδοσία</em>, <em>παράπτωμα</em>, <em>όλος</em>, <em>κάμαρα</em>, <em>πλάτανος</em>, <em>προγραμματισμένος</em>, <em>απολυμαντικός</em>, <em>σύμβαση</em>, <em>χορός</em>, <em>μικροοικονομικός</em>, <em>τζάουλ</em>, <em>απομεινάρι</em>, <em>πρώτος</em></td><td><em>αποδιεθνοποιήσεων</em>, <em>επιστατριών</em>, <em>γαστροοισοφαγικούς</em>, <em>βουτιάς</em>, <em>αλλαντοπώλες</em>, <em>ανασταλτικό</em>, <em>συμβόλαια</em>, <em>γοήτευσα</em>, <em>καρβοξυλική</em>, <em>Βάσω</em>, <em>αστιγματισμούς</em>, <em>μποδίστηκα</em>, <em>θειαιθέρες</em>, <em>αερόβιους</em>, <em>γαλακτικές</em>, <em>αγγειοδιασταλτικοί</em>, <em>διαχωρίζομαι</em>, <em>απασχολήσεων</em>, <em>μοριακό</em>, <em>β΄ συνθ.</em>, <em>τυπική απόκλιση</em>, <em>χημικούς</em>, <em>ατομισμέ</em>, <em>νεαροί</em>, <em>αξύριστες</em></td></tr>
<tr><td>Armenian</td><td><em>կանխել</em>, <em>կարկեհան</em>, <em>առկախ</em>, <em>զեռալ</em>, <em>լուսանցքային</em>, <em>ֆրակ</em>, <em>ձեռնարկել</em>, <em>անկախանալ</em>, <em>հակաօսմանյան</em>, <em>հետևանք</em>, <em>մարդաշատ</em>, <em>պար</em>, <em>բլոգեր</em>, <em>քվազար</em>, <em>համոզել</em>, <em>երբուծ</em>, <em>բավականաչափ</em>, <em>մող</em>, <em>բնակել</em>, <em>նորաշխարհ</em>, <em>կարմիր</em>, <em>սահաթչի</em>, <em>սպառազինություն</em>, <em>ծեփել</em>, <em>պատենտ</em></td><td><em>Բոտսվանա</em>, <em>ՄԱԿ</em>, <em>Որոնտես</em>, <em>դելփին</em>, <em>Մեսրոպյան</em>, <em>անց կենալ</em>, <em>քաղաքական գործիչ</em>, <em>Թորոյան</em>, <em>Աբու Զաբի</em>, <em>Գալճյան</em>, <em>Արաբական Միացյալ Էմիրություններ</em>, <em>ՍՍՀ</em>, <em>Զապորոժիե</em>, <em>Ստեփանյան</em>, <em>վրաններ</em>, <em>հուսո</em>, <em>Աարե</em>, <em>Տիշճյան</em>, <em>ծախսվել</em>, <em>սարեր</em>, <em>Մասերու</em>, <em>Բուդաքյան</em>, <em>պոլի շոր</em>, <em>Ֆլորենցիա</em>, <em>Քիրեմիճյան</em></td></tr>
<tr><td>Albanian</td><td><em>zeshkan</em>, <em>kaptë</em>, <em>currek</em>, <em>absorbim</em>, <em>ujdhesar</em>, <em>gjakës</em>, <em>ftohtësi</em>, <em>ulok</em>, <em>pesëdhjetenjë</em>, <em>tregjysh</em>, <em>kanun</em>, <em>shikoj</em>, <em>zemërim</em>, <em>qepshe</em>, <em>laknëqafe</em>, <em>gërhanë</em>, <em>trajtësoj</em>, <em>mbidialektor</em>, <em>onomatopeik</em>, <em>greth</em>, <em>krinë</em>, <em>zhgjyrç</em>, <em>ekologji</em>, <em>thikëz</em>, <em>meksh</em></td><td><em>cepëra</em>, <em>vorbat</em>, <em>Afrikës</em>, <em>sheu</em>, <em>Kadri</em>, <em>kurvat</em>, <em>Konxhe</em>, <em>xhenxhefila</em>, <em>vegshi</em>, <em>xhamia</em>, <em>cute</em>, <em>zbatica</em>, <em>cahisa</em>, <em>nxura</em>, <em>capokë</em>, <em>përbindëshat</em>, <em>cylaqë</em>, <em>zgavra</em>, <em>Hysenbelliu</em>, <em>Zuzaki</em>, <em>sarkave</em>, <em>mësallat</em>, <em>shkuaka</em>, <em>Tahiri</em>, <em>ushtari</em></td></tr>
<tr><td>Hindi</td><td><em>गंजीफ़ा</em>, <em>मुल्तानी</em>, <em>कोदो</em>, <em>पुनर्जीवित</em>, <em>हिदायत</em>, <em>थोक</em>, <em>प्राचार्या</em>, <em>शुक्ता</em>, <em>सॉकरूओस</em>, <em>दासता</em>, <em>शिकस्त</em>, <em>निरावेशित</em>, <em>राजपूत</em>, <em>प्रशासनिक</em>, <em>कायापलट</em>, <em>हमलावर</em>, <em>ईर्खा</em>, <em>कीकर</em>, <em>अहाब</em>, <em>कड़वापन</em>, <em>इक़रारनामा</em>, <em>प्रत्यावर्ती</em>, <em>चतुर्घात</em>, <em>मिसाल</em>, <em>ग़द्दार</em></td><td><em>चमेलियों</em>, <em>त्रिवेणी नगर</em>, <em>ऍल्युमिनियम</em>, <em>गबरुओं</em>, <em>शीतोष्ण वर्षावन</em>, <em>पिलानेवालीं</em>, <em>निर्धारित करना</em>, <em>सेकती</em>, <em>गाहे-बगाहे</em>, <em>संध्याएँ</em>, <em>सुधारियेगा</em>, <em>मित्रो</em>, <em>मुज़क्कर</em>, <em>जिताके</em>, <em>छेड़ेंगे</em>, <em>खत्री</em>, <em>क़ज़ाक़</em>, <em>चढ़नेवाली</em>, <em>हारेगा</em>, <em>धड़कें</em>, <em>छान</em>, <em>अड़ायेगी</em>, <em>टोंटियों</em>, <em>मिलवायेंगे</em>, <em>पाली</em></td></tr>
<tr><td>Persian</td><td><em>تذکر</em>, <em>نعلبکی</em>, <em>بالین</em>, <em>قاعده</em>, <em>غرفه</em>, <em>نیشکر</em>, <em>رعنا</em>, <em>پاریسی</em>, <em>ضیافت</em>, <em>صادر</em>, <em>رفتار</em>, <em>شهله</em>, <em>جشن</em>, <em>اونطور</em>, <em>سیگارت</em>, <em>جزیه</em>, <em>کوفتن</em>, <em>نبید</em>, <em>گهگاه</em>, <em>باز</em>, <em>سگرنه</em>, <em>زرافه</em>, <em>پنکه</em>, <em>آفتاب‌گردان</em>, <em>منگنه</em></td><td><em>شیر گاو</em>, <em>بلندترین</em>, <em>فاحش‌ترین</em>, <em>درجه‌ها</em>, <em>خراسان</em>, <em>فرنچ پرس</em>, <em>اژه</em>, <em>بخشای</em>, <em>اسم خاص</em>, <em>کورم</em>, <em>حیوون</em>, <em>اعلام کردن</em>, <em>پابرهنگان</em>, <em>یاد دادن</em>, <em>پلاو</em>, <em>سلواکیا</em>, <em>سولاخ</em>, <em>می‌برشتیم</em>, <em>کپان</em>, <em>آیت‌الله‌ها</em>, <em>فلوریدا</em>, <em>می‌آمد</em>, <em>سبک عراقی</em>, <em>تعجب کردن</em>, <em>رفتند</em></td></tr>
<tr><td>Georgian</td><td><em>ქმარი</em>, <em>ოფოფი</em>, <em>მიკროპროცესორი</em>, <em>კრუნჩხვითი</em>, <em>კონუსი</em>, <em>მოსაწყენად</em>, <em>შინაარსიანი</em>, <em>საზრიანი</em>, <em>პრაქტიკული</em>, <em>დაბალპროფილური</em>, <em>გენიტალური</em>, <em>ჰელსინკელი</em>, <em>სათვალიანი</em>, <em>პრეზიდიუმი</em>, <em>თქო</em>, <em>გააჩერებს</em>, <em>ანთრაციტი</em>, <em>აპრიორული</em>, <em>ორმოცდარვა</em>, <em>დავთარი</em>, <em>ნოტიო</em>, <em>ნაყოფიერი</em>, <em>ორე</em>, <em>მოყვარული</em>, <em>თანმხლები</em></td><td><em>ჩეჩნეთი</em>, <em>ნიგერია</em>, <em>ვმღეროდი</em>, <em>სატელიტური სახელმწიფო</em>, <em>აღდგომელაშვილი</em>, <em>საბაზრო ღირებულება</em>, <em>სამხატვრო გალერეა</em>, <em>ბევრეთი</em>, <em>რცხილაფოთლიანი ძელქვა</em>, <em>ღმერთები</em>, <em>დღის</em>, <em>ვითარება</em>, <em>მრავალპარტიული სისტემა</em>, <em>კვანტური გადახლართულობა</em>, <em>ატლანტი</em>, <em>ბინძური კამპანია</em>, <em>პრობლემამ</em>, <em>რუსეთის</em>, <em>სოციალურ-ეკონომიკური</em>, <em>ჰოთ-დოგი</em>, <em>მცენარეები</em>, <em>ტუჩნი</em>, <em>მოიცადე</em>, <em>მგონია</em>, <em>უპ.ყ.</em></td></tr>
<tr><td>Finnish</td><td><em>tarkkaavainen</em>, <em>pääideologi</em>, <em>kuvittaja</em>, <em>yöllä</em>, <em>absoluuttinen</em>, <em>lupahakemus</em>, <em>paikannimi</em>, <em>ympäristöministeriö</em>, <em>singota</em>, <em>laturetki</em>, <em>kili</em>, <em>roomalainen</em>, <em>sapluuna</em>, <em>juustoraaste</em>, <em>tullivirkailija</em>, <em>savuke</em>, <em>vesipullo</em>, <em>tapa</em>, <em>teatraalinen</em>, <em>sopimaton</em>, <em>jalkatila</em>, <em>lisäpalvelu</em>, <em>seerumi</em>, <em>automaatioasentaja</em>, <em>pelimanni</em></td><td><em>gallialaisuuden</em>, <em>ulkoeteinen</em>, <em>viisikymmentäkuusi</em>, <em>jäsenalennus</em>, <em>miestä</em>, <em>takaaladattava</em>, <em>hobitit</em>, <em>taistele</em>, <em>mättäinen</em>, <em>nojapyörä</em>, <em>sallinen</em>, <em>valvoi</em>, <em>satuloiminen</em>, <em>levitetty</em>, <em>känttykahvit</em>, <em>kauppausanssi</em>, <em>alijäähdytään</em>, <em>piispankukka</em>, <em>asuntokauppalaki</em>, <em>ainesana</em>, <em>hakematon</em>, <em>hälytin</em>, <em>rauhaset</em>, <em>amerikkalaistutaan</em>, <em>raukeasti</em></td></tr>
<tr><td>Turkish</td><td><em>cümle</em>, <em>helva</em>, <em>boyayıcı</em>, <em>kartograf</em>, <em>beyazlık</em>, <em>hediyelik</em>, <em>sülale</em>, <em>kuir</em>, <em>dindarlık</em>, <em>çerçeveci</em>, <em>endişeli</em>, <em>kayyım</em>, <em>boğuşmak</em>, <em>derogasyon</em>, <em>pille</em>, <em>fizikokimyasal</em>, <em>töz</em>, <em>urgancı</em>, <em>ayal</em>, <em>akrofobi</em>, <em>söylem</em>, <em>binyıl</em>, <em>triloji</em>, <em>icabet</em>, <em>grup</em></td><td><em>kuşağı</em>, <em>olay güdümlü</em>, <em>İlbey</em>, <em>katyonlar</em>, <em>ditme</em>, <em>gayzerden</em>, <em>yitirme</em>, <em>Batu</em>, <em>filozoflara</em>, <em>evrimlerimizden</em>, <em>sorgular</em>, <em>tirad</em>, <em>ilköğretim okulu</em>, <em>içyüzüm</em>, <em>algoritmama</em>, <em>utandırmak</em>, <em>Yahşihan</em>, <em>yöntemi</em>, <em>yerim</em>, <em>kralın</em>, <em>Tunçsoy</em>, <em>mayınlarından</em>, <em>kaldırılmak</em>, <em>değişkeni</em>, <em>desenim</em></td></tr>
<tr><td>Korean</td><td><em>갑툭튀</em>, <em>인상</em>, <em>양치하다</em>, <em>숨소리</em>, <em>이것</em>, <em>플루오렌</em>, <em>아휴</em>, <em>생각나다</em>, <em>신인</em>, <em>민속</em>, <em>발칙하다</em>, <em>장례</em>, <em>이성애</em>, <em>보전하다</em>, <em>원앙</em>, <em>이성애자</em>, <em>이음매</em>, <em>레루</em>, <em>싱글벙글</em>, <em>포진</em>, <em>모색하다</em>, <em>사각팔방</em>, <em>시신경</em>, <em>요람</em>, <em>너트</em></td><td><em>깊은</em>, <em>아프가니스탄</em>, <em>-이나</em>, <em>아이스 아메리카노</em>, <em>-지요</em>, <em>키갈리</em>, <em>트리니다드 토바고</em>, <em>유니언 잭</em>, <em>해운대</em>, <em>-으믄</em>, <em>소셜 저스티스 워리어</em>, <em>업뎃</em>, <em>콘택트</em>, <em>나블루스</em>, <em>마리오</em>, <em>앵기다</em>, <em>테트라코산</em>, <em>태양계</em>, <em>차우셰스쿠</em>, <em>-에요</em>, <em>생과일 주스</em>, <em>한번</em>, <em>시베리아</em>, <em>거란 소자</em>, <em>깜빠니야</em></td></tr>
<tr><td>Indonesian</td><td><em>memformat</em>, <em>abak</em>, <em>petinju</em>, <em>rumahsakitkan</em>, <em>jati</em>, <em>kasta</em>, <em>esens</em>, <em>wasrey</em>, <em>mikologi</em>, <em>sabun</em>, <em>kres</em>, <em>akuntan</em>, <em>punggah</em>, <em>ereksi</em>, <em>prasarana</em>, <em>bioetika</em>, <em>nekrosis</em>, <em>penuaan</em>, <em>komitmen</em>, <em>berkalung</em>, <em>pesetrum</em>, <em>hidrografer</em>, <em>senggang</em>, <em>emisi</em>, <em>dekat</em></td><td><em>Mugiarto</em>, <em>Sugeng</em>, <em>kenaikan pangkat luar biasa</em>, <em>bungker</em>, <em>kentjana</em>, <em>apam pinang</em>, <em>Paputungan</em>, <em>kota besar</em>, <em>barang siapa</em>, <em>dimotivasi</em>, <em>SPBU</em>, <em>diperbuat</em>, <em>ditipu</em>, <em>ditaklukkan</em>, <em>patju</em>, <em>Bumi</em>, <em>teknik industri</em>, <em>syahadan</em>, <em>merah merang</em>, <em>tata guna</em>, <em>tidur-tidur</em>, <em>kitab undang-undang hukum pidana</em>, <em>alam rendah</em>, <em>walet gua</em>, <em>Aditya</em></td></tr>
<tr><td>Malay</td><td><em>parang</em>, <em>menyusurgalurkan</em>, <em>tua</em>, <em>bura</em>, <em>mangsa</em>, <em>urin</em>, <em>kamul</em>, <em>bepang</em>, <em>keringat</em>, <em>jauhkan</em>, <em>garu</em>, <em>syaitan</em>, <em>sore</em>, <em>baucar</em>, <em>semangat</em>, <em>keterangan</em>, <em>cerpen</em>, <em>pengertian</em>, <em>kuku</em>, <em>penyahpepijat</em>, <em>hadis</em>, <em>semandar</em>, <em>beranggap</em>, <em>sedekah</em>, <em>berabang</em></td><td><em>takse</em>, <em>air seni</em>, <em>Sekinchan</em>, <em>pisang tidak akan berbuah dua kali</em>, <em>uskup agung</em>, <em>-nya</em>, <em>beras belanda</em>, <em>sindrom Klinefelter</em>, <em>empat puluh tujuh</em>, <em>Bentala</em>, <em>selamat Hari Raya</em>, <em>tumbung</em>, <em>tak organik</em>, <em>haji</em>, <em>kayu api</em>, <em>bongkok</em>, <em>sampai nanti</em>, <em>gelam</em>, <em>pari kelawar</em>, <em>abuk</em>, <em>duduk-duduk</em>, <em>siapa-siapa</em>, <em>hak asasi manusia</em>, <em>ahli fikir</em>, <em>Rogayah</em></td></tr>
<tr><td>Arabic</td><td><em>مارستان</em>, <em>لكم</em>, <em>متقارب</em>, <em>اهتدى</em>, <em>يتزمتن</em>, <em>جون</em>, <em>كناسة</em>, <em>مضيرة</em>, <em>منهوب</em>, <em>أنادي</em>, <em>ضحك</em>, <em>همت</em>, <em>نشعر</em>, <em>تخادم</em>, <em>شجعنا</em>, <em>تستأنوا</em>, <em>تبردون</em>, <em>مشمش</em>, <em>تفي</em>, <em>أعيري</em>, <em>يصرفن</em>, <em>فلوكة</em>, <em>انكسوا</em>, <em>مستعمر</em>, <em>تشهدين</em></td><td><em>بدخش</em>, <em>لحج</em>, <em>تولد</em>, <em>جمهورية كوستاريكا</em>, <em>جوبا</em>, <em>المرسلات</em>, <em>تمامة</em>, <em>فانية</em>, <em>قبليون</em>, <em>جيش الدفاع الإسرائيلي</em>, <em>تزييد</em>, <em>شفاه</em>, <em>رئيسية</em>, <em>أتراك</em>, <em>تدهيش</em>, <em>إثمار</em>, <em>ثامر</em>, <em>بغض</em>, <em>مخافر</em>, <em>فعل معتل</em>, <em>نسي</em>, <em>شروب</em>, <em>شفوات</em>, <em>بلاد الزاط</em>, <em>ضغابيس</em></td></tr>
<tr><td>Swahili</td><td><em>hapa</em>, <em>sibu</em>, <em>pisi</em>, <em>roboti</em>, <em>bafu</em>, <em>amali</em>, <em>mtumba</em>, <em>umonaki</em>, <em>msanifu</em>, <em>bisi</em>, <em>lavani</em>, <em>karotini</em>, <em>kiraka</em>, <em>gwiji</em>, <em>rumande</em>, <em>brandi</em>, <em>kivumishi</em>, <em>halaiki</em>, <em>sungura</em>, <em>peponi</em>, <em>uzalendo</em>, <em>mudiri</em>, <em>tawi</em>, <em>mkungumanga</em>, <em>jumuia</em></td><td><em>tulizwa</em>, <em>kujasiri</em>, <em>wadai</em>, <em>awasili</em>, <em>patanisha</em>, <em>vinyota</em>, <em>wasafiri</em>, <em>Irak</em>, <em>kufika</em>, <em>paji la uso</em>, <em>mnaomba</em>, <em>Pili</em>, <em>vinyozi</em>, <em>la chumvi nyingi</em>, <em>Najari</em>, <em>mikuyu</em>, <em>fara</em>, <em>nukta mkato</em>, <em>gawanywa</em>, <em>kuvuta</em>, <em>gilasi</em>, <em>virusi vya papillomavirus ya binadamu</em>, <em>uakifishi</em>, <em>zidiwa</em>, <em>rekebisho</em></td></tr>
</table>
<!-- END:word-samples -->

### Example game chains

The table below shows example chains drawn from simulations, illustrating how the overlap rule plays out across scripts and word structures:

<!-- BEGIN:example-chains -->
<table>
<tr><th>Language</th><th>Example chain</th></tr>
<tr><td>Serbo-Croatian (Latin)</td><td>konvertibilan → antialkoholičarka → kajzerica → carić → iće → ćepanica → cajtung</td></tr>
<tr><td></td><td>pismohrana → nadevati → tisuću → ćutiti → tih → ihtiološki → kirurg</td></tr>
<tr><td></td><td>trup → uporabljiv → ivica → car → argument</td></tr>
<tr><td></td><td>uopšte → termopilski → kijamet → etiopski → kilobajt</td></tr>
<tr><td></td><td>združiti → tipl → plakati → tiskarstvo → voćni → nikdo → događaj → ajnc</td></tr>
<tr><td>Serbo-Croatian (Cyrillic)</td><td>крумпирача → чађ → ађутант</td></tr>
<tr><td></td><td>осовина → наломити → тигањ</td></tr>
<tr><td></td><td>досег → егзосфера → развијати → тишина → наивност → ступац → ацетон → онечишћивач</td></tr>
<tr><td></td><td>јужина → намљети → тиква → васиона → налог → ограничење → његоватељ</td></tr>
<tr><td></td><td>штоперица → цар → аргумент</td></tr>
<tr><td>Macedonian</td><td>достапно → ножница → цајкански → киниса → санхосеанец</td></tr>
<tr><td></td><td>прегази → зимски → километарски → киевјанец</td></tr>
<tr><td></td><td>експериментира → раб → аби → билда → далјан → анемостат → атмосферски → кичевчанец</td></tr>
<tr><td></td><td>армиски → кикс → ксенофобија → јаренец</td></tr>
<tr><td></td><td>седативен → ене → невреден → ендемично → новинар → архитектонски → кингстаунец</td></tr>
<tr><td>Bulgarian</td><td>тарос → осип → ипотека → карфиол → олицетворение</td></tr>
<tr><td></td><td>рецепта → тача → чайник → икона → наркоза → закана → натще → щелия</td></tr>
<tr><td></td><td>девети → тимпан → анархия</td></tr>
<tr><td></td><td>здрав → автодезинфекционен → енергичен → енциклопедия</td></tr>
<tr><td></td><td>познат → атол → олио</td></tr>
<tr><td>Russian</td><td>громко → кофеварка → картография</td></tr>
<tr><td></td><td>изготовлять → тьфу → фужер → ерик → иконопись</td></tr>
<tr><td></td><td>отапливать → тьфу → функционирование → иерархический</td></tr>
<tr><td></td><td>оценщик → икать → тьфу → фуксия</td></tr>
<tr><td></td><td>расформировать → тьфу → фураж → ажурный</td></tr>
<tr><td>Ukrainian</td><td>чаїтися → сяйво → вощити → титул → улюбленець → цькувати → тимчасовий</td></tr>
<tr><td></td><td>безтурботність → тьху → худиківський</td></tr>
<tr><td></td><td>втілювати → тимчасово → ворина → надлишок → окунь</td></tr>
<tr><td></td><td>імперіалізм → зменшуватимуть → тьма → матися → сягнути → тимчасунки → кит</td></tr>
<tr><td></td><td>галиця → цятка → каламар → артеріосклероза → заслужений</td></tr>
<tr><td>Polish</td><td>sałata → tata → tani → nieustraszony → nyt</td></tr>
<tr><td></td><td>archiwista → tajwański → kiczowaty → tymczasowy → wygasać</td></tr>
<tr><td></td><td>czapka → kaszanka → kategoryczny → nyt</td></tr>
<tr><td></td><td>altana → naoczny → nyski → kirgiski → kichać</td></tr>
<tr><td></td><td>szmira → rasowy → wypolerować</td></tr>
<tr><td>Czech</td><td>mediální → nízce → celoživotní → níže → žena → nahoru → runway</td></tr>
<tr><td></td><td>zlepšovací → císařský → kýla → lakomec → echo → honitba → bavič</td></tr>
<tr><td></td><td>zatknout → utopenec → echo → homofobie</td></tr>
<tr><td></td><td>drůbežárna → nahradit → itinerář</td></tr>
<tr><td></td><td>fotit → italský → kýl</td></tr>
<tr><td>Slovak</td><td>garsónka → kanibalizmus → ustavičný</td></tr>
<tr><td></td><td>myšlienka → kameramanský → kýchnuť</td></tr>
<tr><td></td><td>okuliarnik → ikra → rabín</td></tr>
<tr><td></td><td>litrový → výnimka → karpina → natvoriť</td></tr>
<tr><td></td><td>ontogenéza → zavčas → astronautika → kasíno → nový → východný</td></tr>
<tr><td>Lithuanian</td><td>ambasadorius → usnis → ispanė → nėmaž</td></tr>
<tr><td></td><td>kūtvėla → laikinas → astronomija → jazminas → astatis → istorinis → ispanė → nėmaž</td></tr>
<tr><td></td><td>alyvuogė → gėla → laužas → asmenukė → kėlinys</td></tr>
<tr><td></td><td>sutarus → usnis → istorija → jachta → tardavus</td></tr>
<tr><td></td><td>įmotė → tėvavardis → istorija → jauja → japonas → asmenukė → kėlinys</td></tr>
<tr><td>Latvian</td><td>palma → manim → imperiālistiskāks → ksenons</td></tr>
<tr><td></td><td>tieši → šizofrēnija → jautrs</td></tr>
<tr><td></td><td>kontrole → lepnāks → ksenons</td></tr>
<tr><td></td><td>miza → zaķis → islandisks → ksenons</td></tr>
<tr><td></td><td>draiskulis → istaba → baterija → jaukāks → ksenons</td></tr>
<tr><td>German</td><td>Ethiker → erwirtschaften → entsprechend</td></tr>
<tr><td></td><td>Emser → erzielen → entwöhnen → entgegensetzen → entrümpeln</td></tr>
<tr><td></td><td>Nachtgebet → ethisch → chirurgisch → charakterisieren → entwurzelt</td></tr>
<tr><td></td><td>Devise → serienmäßig → igitt</td></tr>
<tr><td></td><td>emporsteigen → entweichen → entwerfen → entwöhnen → entziehen → entstellt</td></tr>
<tr><td>English</td><td>pinter → erythema → matchbox → oxidizing</td></tr>
<tr><td></td><td>milkweed → editable → legged → edginess</td></tr>
<tr><td></td><td>dromedary → ryo → yours</td></tr>
<tr><td></td><td>theoretician → anarchy → hypocrite → tens</td></tr>
<tr><td></td><td>extrinsic → iconography → hyphen → encroachment</td></tr>
<tr><td>Dutch</td><td>zeemonster → erfdeel → elfje → jep → epidermis → islam → amendement</td></tr>
<tr><td></td><td>noordwest → stelselmatig → iglo → lossen → entropie → ieders</td></tr>
<tr><td></td><td>lokken → entourage → gewezen → enkelband</td></tr>
<tr><td></td><td>wreef → efficiëntie → ieders</td></tr>
<tr><td></td><td>ankeren → energiebron → onderduiker → eretitel → eland</td></tr>
<tr><td>Swedish</td><td>dittan → anomali → likvärdig → igenkänningsfaktor → orientering</td></tr>
<tr><td></td><td>arbetsgivare → revolutionera → rakhyvel → elenergi → giga → galopp</td></tr>
<tr><td></td><td>mucka → kardiolog → ogenomtränglig → igenkänningsfaktor → oreglerad → adhd</td></tr>
<tr><td></td><td>mask → skyffel → elitism → smaksak → akilleshäl → älg</td></tr>
<tr><td></td><td>klassificera → radhus → usling</td></tr>
<tr><td>Spanish</td><td>cooperación → ónix → ixil → ilustre → recomendación</td></tr>
<tr><td></td><td>defraudación → ónix → ixil → ilegítimamente → testero → rompedora → radiofrecuencia</td></tr>
<tr><td></td><td>manipulador → organismo → montado → dolencia</td></tr>
<tr><td></td><td>despótico → compensar → arrocero → rosácea</td></tr>
<tr><td></td><td>contraindicación → ónix → ixil → ilusionismo → mortuorio → ionización</td></tr>
<tr><td>French</td><td>biaisé → séchoir → iridium</td></tr>
<tr><td></td><td>héberger → errance → ceinturon → onguent</td></tr>
<tr><td></td><td>siffleur → uriner → erg</td></tr>
<tr><td></td><td>barman → annuler → erg</td></tr>
<tr><td></td><td>provocateur → urine → netteté → télescopage → genièvre → relocalisation → onanisme → merveilleux</td></tr>
<tr><td>Italian</td><td>scuotere → regnare → rendering</td></tr>
<tr><td></td><td>plateale → legnoso → soddisfarlo → lord</td></tr>
<tr><td></td><td>alga → gassoso → sottopagato → tonicità</td></tr>
<tr><td></td><td>funzionale → lene → negatività</td></tr>
<tr><td></td><td>tredici → cinguettare → retrospettivamente → telefonia → iattura → rappresentatività</td></tr>
<tr><td>Portuguese</td><td>obrigada → daltonismo → mongo → goji → jihadista → tataravô → vôo</td></tr>
<tr><td></td><td>decente → terminar → armazenamento → topete → terráqueo</td></tr>
<tr><td></td><td>titubear → arte → terapêutico → congregar → argônio → iodeto → tora → rapidez</td></tr>
<tr><td></td><td>hidromel → elegeram → amnistia → iaque</td></tr>
<tr><td></td><td>indisponível → eloquência → ianque</td></tr>
<tr><td>Romanian</td><td>nesupus → ustura → randare → reocupa → paramedic → icni → nicidecât</td></tr>
<tr><td></td><td>covertă → tăurean → angoasant</td></tr>
<tr><td></td><td>zice → celomat → atrofic → icosaedru → rubăț</td></tr>
<tr><td></td><td>cărturăresc → scâncire → retarda → daltonist → stârv</td></tr>
<tr><td></td><td>sermaia → iahtman → antianticorp</td></tr>
<tr><td>Greek</td><td>ακαζού → ούρο → ροδακινιά</td></tr>
<tr><td></td><td>εμπόρευμα → μαξιλάρα → ραδιοφωνικός</td></tr>
<tr><td></td><td>έθιμο → μούρη → ρηχός</td></tr>
<tr><td></td><td>επιγονατίδα → δανειολήπτρια → ιατρείο</td></tr>
<tr><td></td><td>μαρίδα → δαμασκηνί → νίτρωση → σηκώνω → νωπογραφία</td></tr>
<tr><td>Armenian</td><td>ձմեռել → ելմակ → ակիշ → իշայծյամ → ամերիկուհի → հիասթափություն</td></tr>
<tr><td></td><td>երիվար → արծաթ → աթոռ → ոռնալ → ալկոհոլ → ոլորակ → ակնթարթ</td></tr>
<tr><td></td><td>կասկածելի → լիներ → երթուղային → ինտեգրալ → ալերգիա</td></tr>
<tr><td></td><td>արոր → որակ → ակնածոտ → ոտնապինդ</td></tr>
<tr><td></td><td>արքա → քած → ածիկ</td></tr>
<tr><td>Albanian</td><td>njëzetepesë → sëmur → uroj</td></tr>
<tr><td></td><td>dallë → lëpen → ende → degëz → ëzë → zëvendës</td></tr>
<tr><td></td><td>zgledh → dhaskal → alle → lencol → oler → ereksion → onagër</td></tr>
<tr><td></td><td>dëshmor → oreks → kshetë → tërësisht</td></tr>
<tr><td></td><td>shpet → etje → jeh → ehojo → josh → shëngjinës</td></tr>
<tr><td>Hindi</td><td>हादसा → साक्षात् → त्राता → तालीम</td></tr>
<tr><td></td><td>करी → रीझना → नाना → नाराज़ → ज़वाल</td></tr>
<tr><td></td><td>उखाड़ना → नाना → नाठ</td></tr>
<tr><td></td><td>नियाज़ → ज़िम्मेदारी → रीस</td></tr>
<tr><td></td><td>तिरानवे → वेश्यावृत्ति → तिफ़लाना → नायिका → कालीन</td></tr>
<tr><td>Persian</td><td>جامعه‌شناسی → سیاه → اهمال → الک → لکه → کهنه → نهالی → لیف</td></tr>
<tr><td></td><td>آرم → رمزی → زیرگروه → وهم → هم‌معنی → نیمکت → کتلت</td></tr>
<tr><td></td><td>رمزگشایی → ییلاق → اقتدارگرا → رادیوتراپی → پینگ‌پونگ → نگون → وند → ندانم‌گرایی</td></tr>
<tr><td></td><td>مسافرت → رتبه → بهاریه → یهویی → ییلاق → اقرار → ارادت</td></tr>
<tr><td></td><td>ارجاع → اعتماد → ادکلن → لنگ → نگال → الکترومغناطیس</td></tr>
<tr><td>Georgian</td><td>დიახ → ახალგაზრდულად → ადევნებს</td></tr>
<tr><td></td><td>ჰაერნაოსნობა → ბარკასი → სიგანით → ითესავს → ვსიო → იოგა → გაასწორებს</td></tr>
<tr><td></td><td>კაზაკი → კინოფილმი → მიწისზედა → დაჭიმულად → ადასტურებს</td></tr>
<tr><td></td><td>პანიკური → რიკოშეტი → ტიპურად → ადვილად → ადგილობითი → თილისმა → მაინტერესებს</td></tr>
<tr><td></td><td>სამეცნიერო → რომი → მიდგომა → მარჩბივი → ვიდეო</td></tr>
<tr><td>Finnish</td><td>taidokkaasti → tikkaus → uskoutua</td></tr>
<tr><td></td><td>poimia → iankaikkisesti → tiibetinspanieli → liika → karpalo → loppumaton → onnistua</td></tr>
<tr><td></td><td>vitsikäs → äsh → shoppailla → laukea</td></tr>
<tr><td></td><td>keskeneräisyys → yskittää → äärijärjestö → törkeä</td></tr>
<tr><td></td><td>narratiivi → viivyttely → lyhennelmä → määränpää → äänenlaatu → tunne → nel → eläköön</td></tr>
<tr><td>Turkish</td><td>abarognoz → ozon → ondüle → lengüistik → ikincilik → iklim → imkân</td></tr>
<tr><td></td><td>tezevvüç → üçlü → lüle → lens</td></tr>
<tr><td></td><td>palmiye → yelve → veresiye → yeniden → endirekt</td></tr>
<tr><td></td><td>ikramiye → yemlik → iktisadiyat → atlas → astrolog</td></tr>
<tr><td></td><td>tülü → lütesyum → umursamaz → azık → ıkınmak → akselerasyon → onar → arşın</td></tr>
<tr><td>Korean</td><td>체험 → 험악하다 → 다른</td></tr>
<tr><td></td><td>천식 → 식충이 → 이용 → 용왕 → 왕가 → 가관 → 관용구 → 구렁</td></tr>
<tr><td></td><td>불상 → 상수 → 수상하다 → 다리미 → 미나리 → 리버모륨</td></tr>
<tr><td></td><td>달망구 → 구속 → 속세 → 세륨</td></tr>
<tr><td></td><td>건강 → 강준치 → 치킨너겟</td></tr>
<tr><td>Indonesian</td><td>homonim → impedansi → silt</td></tr>
<tr><td></td><td>mewarnai → aimatatuli → linguis → istiadat → atribusi → simpleks</td></tr>
<tr><td></td><td>tegur → urutan → antraks</td></tr>
<tr><td></td><td>pirau → autistik → ikamah → ahuh</td></tr>
<tr><td></td><td>perhentian → anjan → antinomi → miniatur → urip → ipuh</td></tr>
<tr><td>Malay</td><td>lukah → ahad → adab → abuh</td></tr>
<tr><td></td><td>merakyatkan → anu → nuklear → ardvark</td></tr>
<tr><td></td><td>mendakan → angin → individu → dulang → ngok → okey</td></tr>
<tr><td></td><td>berilium → umur → uranium → umrah → ahad → adik → iktizam → ambulans</td></tr>
<tr><td></td><td>berkahkah → ahmak → aktivitet → etika → karet</td></tr>
<tr><td>Arabic</td><td>تسحر → حرنكش → كشط → شطافة</td></tr>
<tr><td></td><td>مأرب → ربط → بطلتم → تمثل → ثلاثية</td></tr>
<tr><td></td><td>تنافسون → ونش → نشرر</td></tr>
<tr><td></td><td>تنسخوا → واع → اعطسوا → واجهة</td></tr>
<tr><td></td><td>مشرع → رعراع → اعتقدتم → تمارس → رسالة</td></tr>
<tr><td>Swahili</td><td>kuasisi → simiti → tibu → bushuti → tiifu → funda → dahalia</td></tr>
<tr><td></td><td>riboflauini → nikeli → lini → nira → raia</td></tr>
<tr><td></td><td>burudi → divai → aiskrimu → mufti → tisha → hamdia</td></tr>
<tr><td></td><td>mkoromo → momote → teketea</td></tr>
<tr><td></td><td>mkesha → hali → lila → lapa → pambajio → iodini → nimonia</td></tr>
</table>
<!-- END:example-chains -->
