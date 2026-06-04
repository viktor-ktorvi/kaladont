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

<table>
<tr><th>Language</th><th>Surviving words</th><th>Filtered out words</th></tr>
<tr><td>Serbo-Croatian (Latin)</td><td><em>dragan</em>, <em>rumunjski</em>, <em>rasteretiti</em>, <em>tetrijeb</em>, <em>nutrina</em>, <em>scenarij</em>, <em>ceh</e
m>, <em>pohod</em>, <em>izuzetan</em>, <em>huškalo</em>, <em>ćešiti</em>, <em>neuropsihofarmakologija</em>, <em>papirničar</em>, <em>pomoćnik</em>, <em>selen</em>, 
<em>srebrnjak</em>, <em>inatljivo</em>, <em>imitacija</em>, <em>kamičak</em>, <em>razbuđivati</em>, <em>livreja</em>, <em>onečistiti</em>, <em>albanološkinja</em>, 
<em>ker</em>, <em>otkopčan</em></td><td><em>zajašiti</em>, <em>očevi</em>, <em>Janja</em>, <em>tepemo</em>, <em>Island</em>, <em>muči</em>, <em>stogom</em>, <em>tac
no</em>, <em>zemljotresu</em>, <em>vazali</em>, <em>jarče</em>, <em>pasena</em>, <em>ločimo</em>, <em>mamila</em>, <em>morski šipak</em>, <em>Jašarević</em>, <em>dunem</em>, <em>kosku</em>, <em>svarene</em>, <em>davio</em>, <em>udalo</em>, <em>gorko</em>, <em>bacani</em>, <em>pojavio</em>, <em>veštu</em></td></tr>
<tr><td>Serbo-Croatian (Cyrillic)</td><td><em>шведски</em>, <em>дуговјечан</em>, <em>растављати</em>, <em>збијати</em>, <em>машинерија</em>, <em>диплоидан</em>, <em
>напето</em>, <em>самооплођивање</em>, <em>глагољица</em>, <em>прецизно</em>, <em>кретенизација</em>, <em>половина</em>, <em>кријумчарство</em>, <em>прашак</em>, <e
m>бод</em>, <em>фотоотпорник</em>, <em>заокружити</em>, <em>светиште</em>, <em>јунски</em>, <em>лажност</em>, <em>катастрофалан</em>, <em>решење</em>, <em>искоришта
вати</em>, <em>сумњичав</em>, <em>разломити</em></td><td><em>изоравати</em>, <em>Мексиканац</em>, <em>Крешевљанин</em>, <em>Јован</em>, <em>Сисак</em>, <em>нагртати
</em>, <em>Саудијац</em>, <em>Бечкерек</em>, <em>-ило</em>, <em>Суданац</em>, <em>малинама</em>, <em>стићи</em>, <em>Копарштина</em>, <em>баласту</em>, <em>Андорац<
/em>, <em>подстакнути</em>, <em>Жепче</em>, <em>доодење</em>, <em>мешће</em>, <em>дооде</em>, <em>антик</em>, <em>мог</em>, <em>стрн</em>, <em>Земљин</em>, <em>-ист</em></td></tr>
<tr><td>Macedonian</td><td><em>неотстаплив</em>, <em>кандидира</em>, <em>недостоинствено</em>, <em>непоткренат</em>, <em>урнек</em>, <em>помавта</em>, <em>пропаст</
em>, <em>недозволив</em>, <em>карбонизација</em>, <em>колокација</em>, <em>страв</em>, <em>попишувач</em>, <em>колеџ</em>, <em>кикиришка</em>, <em>несотрен</em>, <e
m>лаик</em>, <em>кафен</em>, <em>незаштитено</em>, <em>маршалски</em>, <em>срамни</em>, <em>идила</em>, <em>лежи</em>, <em>победува</em>, <em>квасец</em>, <em>делта
</em></td><td><em>Злата</em>, <em>повеликодушен</em>, <em>наоблачување</em>, <em>додворување</em>, <em>елени</em>, <em>зашеметен</em>, <em>се врати</em>, <em>реклам
и</em>, <em>компјутерџии</em>, <em>цветче</em>, <em>се искака</em>, <em>скаран</em>, <em>подзамрзнат</em>, <em>телепортиран</em>, <em>набиен</em>, <em>се состои</em
>, <em>вакцини</em>, <em>препрочитуван</em>, <em>фишечиште</em>, <em>дојавуван</em>, <em>басамаци</em>, <em>идентификување</em>, <em>насапунување</em>, <em>поштенско сандаче</em>, <em>рестораниште</em></td></tr>
<tr><td>Bulgarian</td><td><em>обръгвам</em>, <em>птичар</em>, <em>леди</em>, <em>върховие</em>, <em>перач</em>, <em>порт</em>, <em>проводник</em>, <em>лаптоп</em>, 
<em>изчисление</em>, <em>колеж</em>, <em>регион</em>, <em>наустник</em>, <em>неприязън</em>, <em>шантажирам</em>, <em>ларва</em>, <em>ридая</em>, <em>перигей</em>, 
<em>произтичащия</em>, <em>ерген</em>, <em>оръдие</em>, <em>акростишен</em>, <em>полза</em>, <em>хоплит</em>, <em>шарен</em>, <em>рибояд</em></td><td><em>четиридесе
т и две</em>, <em>лъвице</em>, <em>победяла</em>, <em>абортирайте</em>, <em>ометат</em>, <em>легализирания</em>, <em>зачетяхме</em>, <em>разхождащо</em>, <em>опасли
</em>, <em>припадаше</em>, <em>костурче</em>, <em>сушащо</em>, <em>потънахме</em>, <em>коронясай</em>, <em>отровилото</em>, <em>бъбар</em>, <em>изгризалата</em>, <em>обковавано</em>, <em>отсъстващ</em>, <em>изсечал</em>, <em>винене</em>, <em>администрацийо</em>, <em>дръвчета</em>, <em>трънак</em>, <em>клюнове</em></td></tr>   
<tr><td>Russian</td><td><em>провинность</em>, <em>дорогуша</em>, <em>концентрационный</em>, <em>раскраска</em>, <em>порознь</em>, <em>преобладание</em>, <em>немалов
ажный</em>, <em>всыпать</em>, <em>салак</em>, <em>поплавать</em>, <em>верба</em>, <em>буквоед</em>, <em>логично</em>, <em>видимость</em>, <em>нулевой</em>, <em>убра
нство</em>, <em>астролябия</em>, <em>менопауза</em>, <em>редис</em>, <em>сервировка</em>, <em>крестить</em>, <em>суммарный</em>, <em>фонтан</em>, <em>саркастический
</em>, <em>эвкалипт</em></td><td><em>издольщин</em>, <em>порадеют</em>, <em>замедли</em>, <em>милосердиях</em>, <em>уравниваю</em>, <em>стилизаций</em>, <em>уплачив
ает</em>, <em>тверки</em>, <em>лексемах</em>, <em>изваяла</em>, <em>вылито</em>, <em>накрапывали</em>, <em>восьмиугольнике</em>, <em>прапрапрадед</em>, <em>комиксам
и</em>, <em>солнцестояниям</em>, <em>Исикари</em>, <em>шорный</em>, <em>опорожнении</em>, <em>позванивал</em>, <em>шеломам</em>, <em>цинках</em>, <em>приготавливаюсь</em>, <em>инцидентами</em>, <em>плову</em></td></tr>
<tr><td>Ukrainian</td><td><em>поема</em>, <em>чергуватися</em>, <em>материнство</em>, <em>відтак</em>, <em>рибальство</em>, <em>синельниківський</em>, <em>вирішення
</em>, <em>оригінальний</em>, <em>ворог</em>, <em>авіаобприскування</em>, <em>шопінг</em>, <em>українськість</em>, <em>хрестоматійний</em>, <em>мармеляда</em>, <em>
шик</em>, <em>біоматеріал</em>, <em>акулячий</em>, <em>нереалістичний</em>, <em>ждати</em>, <em>відро</em>, <em>ковтун</em>, <em>впадати</em>, <em>галактика</em>, <
em>повечеряти</em>, <em>горе</em></td><td><em>виконають</em>, <em>навколишнє</em>, <em>оранжеву</em>, <em>обчислювальну</em>, <em>першопрохідця</em>, <em>оцінок</em
>, <em>вроду</em>, <em>залоги</em>, <em>чухай</em>, <em>Шостка</em>, <em>вуличну</em>, <em>феєрверкові</em>, <em>Трійця</em>, <em>дешеве</em>, <em>вирішування</em>,
 <em>усміхаймося</em>, <em>укриття</em>, <em>найскладніші</em>, <em>ефективних</em>, <em>Лисівці</em>, <em>художньому</em>, <em>проведу</em>, <em>йодований</em>, <em>Бранденбурзькі ворота</em>, <em>бесіди</em></td></tr>
<tr><td>Polish</td><td><em>podobać</em>, <em>manewrowy</em>, <em>triathlon</em>, <em>cebula</em>, <em>zobowiązany</em>, <em>mężny</em>, <em>aranżer</em>, <em>przynę
ta</em>, <em>ratować</em>, <em>dziura</em>, <em>semafor</em>, <em>wpędzić</em>, <em>szczodrze</em>, <em>sejf</em>, <em>sztorm</em>, <em>unieść</em>, <em>suplement</
em>, <em>sierota</em>, <em>organizacyjny</em>, <em>nierozpuszczalny</em>, <em>barber</em>, <em>dostateczny</em>, <em>kisiel</em>, <em>staroć</em>, <em>próba</em></t
d><td><em>krótkowąs</em>, <em>podrywałaby</em>, <em>wądołami</em>, <em>mleczan</em>, <em>gotujmy</em>, <em>odwiedzałbym</em>, <em>Zwoliński</em>, <em>poboruchać</em
>, <em>najciemniej</em>, <em>welociraptor</em>, <em>rwetes</em>, <em>nawiew</em>, <em>wyminąwszy</em>, <em>słusny</em>, <em>wspaniałej</em>, <em>stratyfikować</em>,
 <em>północnomacedońską</em>, <em>symulowało</em>, <em>słałeś</em>, <em>ciężarach</em>, <em>podlewałabyś</em>, <em>kromeczką</em>, <em>gorący kartofel</em>, <em>kontenta</em>, <em>senną</em></td></tr>
<tr><td>Czech</td><td><em>následník</em>, <em>březový</em>, <em>herpes</em>, <em>svádění</em>, <em>kopáč</em>, <em>předplacený</em>, <em>bubeník</em>, <em>hlasatel<
/em>, <em>cvičák</em>, <em>převratný</em>, <em>uhel</em>, <em>spotřebič</em>, <em>degradovat</em>, <em>ladný</em>, <em>tesařství</em>, <em>čelovka</em>, <em>nehořla
vý</em>, <em>lýko</em>, <em>pojistné</em>, <em>vášnivý</em>, <em>pošetilý</em>, <em>scenárista</em>, <em>foťák</em>, <em>nábytek</em>, <em>bezcelní</em></td><td><em
>obyvatelům</em>, <em>křivé</em>, <em>Radvan</em>, <em>zpustly</em>, <em>rozlišovatelný</em>, <em>Besarábie</em>, <em>arkussinus</em>, <em>loutnička</em>, <em>besed
ník</em>, <em>zorá</em>, <em>kazili</em>, <em>vévodkyních</em>, <em>řídící znak</em>, <em>hnisavý vřed</em>, <em>jestřábník</em>, <em>toulky</em>, <em>opakování</em>, <em>pře</em>, <em>Dobroslav</em>, <em>žeh</em>, <em>-nice</em>, <em>katalýza</em>, <em>nezdravá</em>, <em>medák</em>, <em>Kudláč</em></td></tr>
<tr><td>Slovak</td><td><em>galéria</em>, <em>pevnosť</em>, <em>jarmový</em>, <em>štetec</em>, <em>sirôtka</em>, <em>sklo</em>, <em>politika</em>, <em>činža</em>, <e
m>altruizmus</em>, <em>hŕba</em>, <em>čepiec</em>, <em>patizón</em>, <em>hlohový</em>, <em>altsaxofón</em>, <em>charizmaticky</em>, <em>miestnosť</em>, <em>histopat
ológia</em>, <em>entuziastický</em>, <em>dobro</em>, <em>rezeň</em>, <em>amnézia</em>, <em>dula</em>, <em>kotúľ</em>, <em>juhás</em>, <em>afatický</em></td><td><em>
Mareš</em>, <em>Miškech</em>, <em>krajine</em>, <em>rekordmaniek</em>, <em>mala</em>, <em>učňami</em>, <em>patria</em>, <em>laze</em>, <em>Želmíra</em>, <em>dňami</
em>, <em>čižmička</em>, <em>rybárka</em>, <em>Bern</em>, <em>žúrmi</em>, <em>charakteru</em>, <em>gúľaj</em>, <em>hrdinami</em>, <em>menší</em>, <em>Karovič</em>, <em>Bába</em>, <em>Fišer</em>, <em>zlodejovi</em>, <em>nej</em>, <em>kobier</em>, <em>elektroterapiou</em></td></tr>
<tr><td>Lithuanian</td><td><em>šarvas</em>, <em>dėkoju</em>, <em>kapueira</em>, <em>moterius</em>, <em>kiras</em>, <em>svajonė</em>, <em>kepti</em>, <em>vetušas</em
>, <em>saitas</em>, <em>ciklas</em>, <em>paslaptingai</em>, <em>garantija</em>, <em>išmokti</em>, <em>gaubti</em>, <em>pirmokė</em>, <em>patogus</em>, <em>golfas</e
m>, <em>paupys</em>, <em>kompetentingas</em>, <em>ilgai</em>, <em>baronas</em>, <em>sėdėti</em>, <em>ieškoti</em>, <em>registruoti</em>, <em>kūryba</em></td><td><em
>estiškojo</em>, <em>nekenčiau</em>, <em>šiknarankėmis</em>, <em>švelnesniame</em>, <em>smulkmeniškuosius</em>, <em>Vilniumi</em>, <em>haliucinuosiančiai</em>, <em>
Apolono</em>, <em>seniausiojoje</em>, <em>dieviškesniųjų</em>, <em>mįslingesnę</em>, <em>Tunisas</em>, <em>duosiančiąja</em>, <em>švelnesnėmis</em>, <em>pripratote<
/em>, <em>švelnesnis</em>, <em>atkeliaujančiąsias</em>, <em>izotopą</em>, <em>myžąs</em>, <em>suprastas</em>, <em>vaizdingumus</em>, <em>seilėkime</em>, <em>duosiančiosiose</em>, <em>atkeliaudavęs</em>, <em>paradoksų</em></td></tr>
<tr><td>Latvian</td><td><em>fašists</em>, <em>laisks</em>, <em>latīniskāk</em>, <em>censīgāks</em>, <em>intoksikācija</em>, <em>dancināts</em>, <em>nākam</em>, <em>
interesants</em>, <em>vislokāk</em>, <em>blāvodams</em>, <em>neskatot</em>, <em>elektrostacija</em>, <em>paslēpjošs</em>, <em>diennakts</em>, <em>visnedzirdīgākais<
/em>, <em>nestāvēšana</em>, <em>fotogrāfiski</em>, <em>reālisms</em>, <em>dzīvi</em>, <em>neitrālāks</em>, <em>bezjēdzīgāk</em>, <em>aploks</em>, <em>neņemam</em>, 
<em>vienpadsmit</em>, <em>slimīgs</em></td><td><em>rūpīgāk</em>, <em>ledus lāča</em>, <em>mirušajās</em>, <em>rupjām vīlēm</em>, <em>slimībai</em>, <em>neabstrahējo
šām</em>, <em>vismīļākie</em>, <em>apmainītā</em>, <em>vispasīvākajās</em>, <em>bučojamus</em>, <em>baznices</em>, <em>visbrīvākajās</em>, <em>īsākās</em>, <em>danč
i</em>, <em>rīks</em>, <em>atvainojušiem</em>, <em>visutainākajai</em>, <em>biezas</em>, <em>labās</em>, <em>Aleksandrs</em>, <em>gaumīga</em>, <em>netīrīgie</em>, <em>nešuvāt</em>, <em>visazerbaidžāniskākajā</em>, <em>nesarkdamas</em></td></tr>
<tr><td>German</td><td><em>schnorren</em>, <em>Vorfreude</em>, <em>Agnostizismus</em>, <em>Sago</em>, <em>Vertragsrecht</em>, <em>Ausdrucksweise</em>, <em>Kolumnist
</em>, <em>übergreifen</em>, <em>Führerstand</em>, <em>hundert</em>, <em>Kongress</em>, <em>bauen</em>, <em>Alias</em>, <em>darlegen</em>, <em>angstvoll</em>, <em>b
egeben</em>, <em>Aal</em>, <em>blendend</em>, <em>warm</em>, <em>Bürotür</em>, <em>Draisine</em>, <em>Unwahrheit</em>, <em>imprägnieren</em>, <em>stören</em>, <em>L
ungenödem</em></td><td><em>maledeien</em>, <em>betriebsratsverseuchtem</em>, <em>halfst mit</em>, <em>Grotten</em>, <em>Jahrhundertende</em>, <em>beunruhigte</em>, 
<em>talmudischeres</em>, <em>Achtelfinal</em>, <em>Pilzrahmsuppe</em>, <em>führte</em>, <em>fusskrank</em>, <em>S-Bootes</em>, <em>Brotkarte</em>, <em>beantragt</em
>, <em>Wertbegriffes</em>, <em>Mikrophons</em>, <em>mittelmäßiger</em>, <em>exorzierst</em>, <em>unsanfterer</em>, <em>neuer</em>, <em>halsabschneiderischerem</em>, <em>Wurstscheiben</em>, <em>umtauschend</em>, <em>brach auseinander</em>, <em>Umweltauswirkung</em></td></tr>
<tr><td>English</td><td><em>crone</em>, <em>salaried</em>, <em>animated</em>, <em>lauding</em>, <em>waterlogged</em>, <em>fray</em>, <em>sleepwalking</em>, <em>grit
</em>, <em>roleplaying</em>, <em>equity</em>, <em>inviting</em>, <em>fortunate</em>, <em>nuk</em>, <em>shanty</em>, <em>prosocial</em>, <em>overstock</em>, <em>nonc
onformist</em>, <em>cappuccino</em>, <em>sociolinguistic</em>, <em>pinus</em>, <em>shinkansen</em>, <em>immortal</em>, <em>bayless</em>, <em>grab</em>, <em>universa
list</em></td><td><em>choky</em>, <em>toadstool leather coral</em>, <em>asparagusate</em>, <em>compliest</em>, <em>ashwagandha</em>, <em>maasbanker</em>, <em>longil
oquence</em>, <em>nontherapy</em>, <em>the damage is done</em>, <em>botanists</em>, <em>flexor carpi radialis</em>, <em>Garibaldi biscuits</em>, <em>motion-pictures
</em>, <em>exatons</em>, <em>Sians</em>, <em>money spell</em>, <em>grapled</em>, <em>transplantologist</em>, <em>perthiocyanate</em>, <em>toparch</em>, <em>counterpicketer</em>, <em>in no time</em>, <em>blazen</em>, <em>brain fluid</em>, <em>full metal jacket</em></td></tr>
<tr><td>Dutch</td><td><em>werkkamer</em>, <em>meedogenloos</em>, <em>econoom</em>, <em>drukwerk</em>, <em>amuse</em>, <em>veiligheidsdienst</em>, <em>zomers</em>, <
em>opbracht</em>, <em>opbouw</em>, <em>verzinnen</em>, <em>gelijkwaardigheid</em>, <em>opzien</em>, <em>dokter</em>, <em>bestuurbaar</em>, <em>calorie</em>, <em>toi
letpapier</em>, <em>landbouwbeleid</em>, <em>rozenbottel</em>, <em>sparren</em>, <em>regio</em>, <em>vaste</em>, <em>berusten</em>, <em>aandrukken</em>, <em>kunnen<
/em>, <em>rechts</em></td><td><em>bedinging</em>, <em>cowboykapitalisme</em>, <em>verplegers</em>, <em>dolf</em>, <em>miste</em>, <em>Noordkant</em>, <em>kansen</em
>, <em>verlangzaamt</em>, <em>geprolongeerd</em>, <em>bedoven</em>, <em>romusha</em>, <em>Rooi Afo</em>, <em>mortuariums</em>, <em>ingrave</em>, <em>gedichtjes</em>
, <em>-noom</em>, <em>37ste</em>, <em>terugbrachten</em>, <em>bepeinze</em>, <em>verschanste</em>, <em>ingestonken</em>, <em>loop om</em>, <em>De Knijp</em>, <em>herkrijgen</em>, <em>voorbipsje</em></td></tr>
<tr><td>Swedish</td><td><em>bann</em>, <em>radio</em>, <em>sallad</em>, <em>bokskog</em>, <em>befogenhet</em>, <em>handbollsmatch</em>, <em>halta</em>, <em>kristall
glas</em>, <em>briljera</em>, <em>gatubarn</em>, <em>smeka</em>, <em>komplexitet</em>, <em>ypperligt</em>, <em>vetenskapsjournalist</em>, <em>blomma</em>, <em>envis
as</em>, <em>underförstådd</em>, <em>slutanvändare</em>, <em>avlida</em>, <em>varningsskott</em>, <em>begynnelse</em>, <em>årgång</em>, <em>femtio</em>, <em>kollaps
</em>, <em>nödlanda</em></td><td><em>förvaringsutrymmets</em>, <em>biltäthetens</em>, <em>kostnadsökningarnas</em>, <em>kapplöpningsbanors</em>, <em>ögonblicket</em
>, <em>giljotinernas</em>, <em>tågolyckans</em>, <em>sångsparvarna</em>, <em>påtvingar</em>, <em>plikttrogna</em>, <em>bebisars</em>, <em>praktmalvan</em>, <em>skru
darna</em>, <em>betalsystemen</em>, <em>kamtjatkakrabbas</em>, <em>åskvädrens</em>, <em>lockvaras</em>, <em>numreringar</em>, <em>blodregn</em>, <em>knapptelefonens</em>, <em>manschetten</em>, <em>inbegripne</em>, <em>sammanhängt</em>, <em>nygrekiskt</em>, <em>litteraturens</em></td></tr>
<tr><td>Spanish</td><td><em>aluminio</em>, <em>quejarse</em>, <em>barranco</em>, <em>tinto</em>, <em>cosmopolita</em>, <em>primicia</em>, <em>pacto</em>, <em>contra
riamente</em>, <em>gajo</em>, <em>insistente</em>, <em>deporte</em>, <em>comprometida</em>, <em>urraca</em>, <em>escayola</em>, <em>pensamiento</em>, <em>funcional<
/em>, <em>deshuesado</em>, <em>tempo</em>, <em>contrincante</em>, <em>exhibir</em>, <em>chocante</em>, <em>meada</em>, <em>ahijado</em>, <em>salchichón</em>, <em>sk
ate</em></td><td><em>acetifiquéis</em>, <em>auscultándose</em>, <em>establecidas</em>, <em>genuidad</em>, <em>remeciéndome</em>, <em>ostrería</em>, <em>abultadísima
</em>, <em>aterrorizase</em>, <em>dañare</em>, <em>chambearías</em>, <em>cotos</em>, <em>candaran</em>, <em>aturquesado</em>, <em>escalarme</em>, <em>seleniforme</e
m>, <em>renguearéis</em>, <em>aplatanabas</em>, <em>polinizadora</em>, <em>evanescés</em>, <em>anglicanizarme</em>, <em>lengüeteáremos</em>, <em>exclamaste</em>, <em>queñuales</em>, <em>cetoácido</em>, <em>retipificaras</em></td></tr>
<tr><td>French</td><td><em>thaï</em>, <em>rature</em>, <em>partir</em>, <em>nouvellement</em>, <em>sténographe</em>, <em>bégayer</em>, <em>différenciation</em>, <em
>rafle</em>, <em>archiduc</em>, <em>orange</em>, <em>bellot</em>, <em>vieillissant</em>, <em>hivernal</em>, <em>brandon</em>, <em>virer</em>, <em>propulsion</em>, <
em>tchécoslovaque</em>, <em>cadavre</em>, <em>porto</em>, <em>pipi</em>, <em>électroménager</em>, <em>fatal</em>, <em>adéquat</em>, <em>stimuler</em>, <em>décodage<
/em></td><td><em>droits de l'homme</em>, <em>désagrafassiez</em>, <em>puniciques</em>, <em>endivisionna</em>, <em>caravelles</em>, <em>empileriez</em>, <em>garder s
on calme</em>, <em>soûlions</em>, <em>réécrivirent</em>, <em>surfaciques</em>, <em>interdiras</em>, <em>rebaptises</em>, <em>correspondant</em>, <em>aromatisés</em>
, <em>excrèteras</em>, <em>amaranthe</em>, <em>offrant</em>, <em>reflétassions</em>, <em>dallé</em>, <em>tire-au-flanc</em>, <em>parrainai</em>, <em>il n'y a pas de quoi fouetter un chat</em>, <em>manœuvrai</em>, <em>Béziers</em>, <em>marcherez</em></td></tr>
<tr><td>Italian</td><td><em>consenziente</em>, <em>serialità</em>, <em>sistematicamente</em>, <em>spensierato</em>, <em>mononucleosi</em>, <em>rostro</em>, <em>armi
stizio</em>, <em>carezza</em>, <em>incancellabile</em>, <em>linkare</em>, <em>databile</em>, <em>cercarli</em>, <em>elettivo</em>, <em>uscio</em>, <em>mutevolezza</
em>, <em>carnera</em>, <em>solitario</em>, <em>lampone</em>, <em>diramare</em>, <em>villano</em>, <em>prepensionamento</em>, <em>ulti</em>, <em>sfilza</em>, <em>rec
arci</em>, <em>donnino</em></td><td><em>risaltavamo</em>, <em>conculcabile</em>, <em>eflornitine</em>, <em>strangolate</em>, <em>spopolandovi</em>, <em>pagavo</em>,
 <em>Rodinò</em>, <em>allacciassi</em>, <em>radiologhe</em>, <em>divertivo</em>, <em>fiocinammo</em>, <em>sgrigiato</em>, <em>sposseggano</em>, <em>lofoforo</em>, <
em>autopubblichiamo</em>, <em>maturanda</em>, <em>bilanciavi</em>, <em>trascinano</em>, <em>lisciassero</em>, <em>anglonormanna</em>, <em>ombrellificio</em>, <em>permanentato</em>, <em>assiemi</em>, <em>odografi</em>, <em>rovisteresti</em></td></tr>
<tr><td>Portuguese</td><td><em>voador</em>, <em>deliberadamente</em>, <em>condão</em>, <em>live</em>, <em>radiológico</em>, <em>atingir</em>, <em>mol</em>, <em>gulo
so</em>, <em>empurraram</em>, <em>relaxante</em>, <em>átrio</em>, <em>cidade</em>, <em>retranca</em>, <em>regozijo</em>, <em>flatulência</em>, <em>fluorescente</em>
, <em>genoma</em>, <em>snowboard</em>, <em>prol</em>, <em>salvaguardar</em>, <em>processador</em>, <em>deão</em>, <em>arquitetónico</em>, <em>fuste</em>, <em>barra<
/em></td><td><em>encriptaste</em>, <em>tosaram</em>, <em>zerar a vida</em>, <em>lépida</em>, <em>delinquias</em>, <em>bainhámos</em>, <em>veredicto</em>, <em>cromem
</em>, <em>eternizava</em>, <em>pensionada</em>, <em>academizáramos</em>, <em>ganirem</em>, <em>boqui-aberta</em>, <em>sonambuleis</em>, <em>alcoolemia</em>, <em>op
primiu</em>, <em>baitariam</em>, <em>desacopláveis</em>, <em>contratares</em>, <em>Dubrovnik</em>, <em>lamuriará</em>, <em>quadriculado</em>, <em>logaste</em>, <em>engolirás</em>, <em>Furukawa</em></td></tr>
<tr><td>Romanian</td><td><em>solniță</em>, <em>pisoi</em>, <em>oniric</em>, <em>lanametru</em>, <em>primordie</em>, <em>harghitean</em>, <em>jăratic</em>, <em>pușki
nian</em>, <em>termorezistent</em>, <em>benedicțiune</em>, <em>histerometru</em>, <em>otrăvire</em>, <em>anartrie</em>, <em>sprijin</em>, <em>magnetizat</em>, <em>i
zogeoterm</em>, <em>ricanare</em>, <em>kurd</em>, <em>crescând</em>, <em>frigăruică</em>, <em>săritură</em>, <em>mobilizabil</em>, <em>peștiman</em>, <em>diurn</em>
, <em>adaptabilitate</em></td><td><em>chircit</em>, <em>ferestraș mic</em>, <em>banano</em>, <em>Șcheia</em>, <em>Șilea</em>, <em>cardiologe</em>, <em>cișmă</em>, <
em>scrietor</em>, <em>termen generic</em>, <em>Bâstroe</em>, <em>densitate de sarcină</em>, <em>recopiat</em>, <em>Gura Bâdiliței</em>, <em>dobrogeancă</em>, <em>No
vosiolovca</em>, <em>microbiologa</em>, <em>bombat</em>, <em>chirioară</em>, <em>Băluța</em>, <em>jurisdicții</em>, <em>mijlocaș ofensiv</em>, <em>pisici</em>, <em>Hobaia</em>, <em>golful</em>, <em>Tăutu</em></td></tr>
<tr><td>Greek</td><td><em>προσκοπιμότητα</em>, <em>ξεσπίτωμα</em>, <em>επαναφέρω</em>, <em>βοήθεια</em>, <em>οκτακοσιοστός</em>, <em>ρεσεψιόν</em>, <em>αφουγκράζομα
ι</em>, <em>αγκουρέτο</em>, <em>οικοτοξικολογία</em>, <em>ανεπιστημοσύνη</em>, <em>θετικός</em>, <em>αχρέωτος</em>, <em>βραζιλιάνικος</em>, <em>αστή</em>, <em>στρίβ
ομαι</em>, <em>μπακάλικο</em>, <em>αποσχισμένος</em>, <em>σμίλη</em>, <em>αιδοίο</em>, <em>σκεπάζω</em>, <em>αλευρόγαια</em>, <em>χορευτής</em>, <em>ουρηθροσκοπία</
em>, <em>ασπρόμαυρο</em>, <em>αεί</em></td><td><em>ψόφε</em>, <em>υπερφυσικές</em>, <em>δικές</em>, <em>ψάχτηκα</em>, <em>χορέψανε</em>, <em>μύτες</em>, <em>αντοχών
</em>, <em>σαββατοκύριακων</em>, <em>αμέλησα</em>, <em>σιδέρωσα</em>, <em>αρχηγίνες</em>, <em>πρόβιος</em>, <em>αιγό-</em>, <em>αγκομαχητών</em>, <em>δυνατούς</em>,
 <em>αντιμιλιταρισμούς</em>, <em>αιχμής</em>, <em>βαριόμασταν</em>, <em>αμφισβητήσεως</em>, <em>αεροστεγή</em>, <em>υμνήσω</em>, <em>αλεύρων</em>, <em>Αθιγγάνων</em>, <em>βεβαιότερης</em>, <em>συγκεκριμένο</em></td></tr>
<tr><td>Armenian</td><td><em>խոհանոց</em>, <em>տարատեսակ</em>, <em>կենալ</em>, <em>կոմունիկացիա</em>, <em>սրբել</em>, <em>դաստակերտ</em>, <em>ժեստ</em>, <em>էտրուսկ
երեն</em>, <em>ձայնարկիչ</em>, <em>քարայր</em>, <em>ուսում</em>, <em>ցեղակրոնություն</em>, <em>ֆլեյտա</em>, <em>առկայծում</em>, <em>մազալու</em>, <em>բարձունք</em>,
 <em>կրթաթոշակ</em>, <em>ճամփորդական</em>, <em>նմանապես</em>, <em>մշկընկույզ</em>, <em>քարտեզագրական</em>, <em>լորձունք</em>, <em>ամեն</em>, <em>օթարան</em>, <em>առ
ակախոս</em></td><td><em>աղջիկներ</em>, <em>կուտեի</em>, <em>Ռայպուր</em>, <em>Նորատունկ</em>, <em>եղինջներ</em>, <em>Իյնէճեան</em>, <em>Քարոն</em>, <em>խոսքերով</em
>, <em>Սարդինիա</em>, <em>Հայտոսթյան</em>, <em>ինչ կա չկա</em>, <em>Ջեյմս Բոնդ</em>, <em>Աղդամ</em>, <em>գեղեցկուհին</em>, <em>Շահինյան</em>, <em>գուշակվել</em>, <e
m>Բիրմինհամ</em>, <em>Այար Ռաջա</em>, <em>գործեր</em>, <em>ԱԱՌ</em>, <em>Հինդուստան</em>, <em>Անի</em>, <em>ժանի</em>, <em>լիւն</em>, <em>մարդասպաններ</em></td></tr>
<tr><td>Albanian</td><td><em>rrënoj</em>, <em>fabrikë</em>, <em>dëngla</em>, <em>mbret</em>, <em>gëlqere</em>, <em>kombëtar</em>, <em>armatë</em>, <em>normalitet</e
m>, <em>namaz</em>, <em>kërrlë</em>, <em>ndore</em>, <em>mashë</em>, <em>vetiu</em>, <em>gri</em>, <em>gjeometri</em>, <em>murgash</em>, <em>sevda</em>, <em>autor</
em>, <em>harmi</em>, <em>thith</em>, <em>arësyetoj</em>, <em>njëkohës</em>, <em>kult</em>, <em>trullos</em>, <em>tall</em></td><td><em>qiraxhinj</em>, <em>Liridon</
em>, <em>ndenjke</em>, <em>Kujtim</em>, <em>hallash</em>, <em>Ilir</em>, <em>Ajteni</em>, <em>Etrit</em>, <em>boshtra</em>, <em>njerëzit</em>, <em>talla</em>, <em>Z
hitia</em>, <em>populli</em>, <em>rrëbythem</em>, <em>zhavorresh</em>, <em>krinë</em>, <em>Sheval</em>, <em>Gjimshiti</em>, <em>fsheha</em>, <em>afërditë</em>, <em>mrekullitë</em>, <em>bregdeteve</em>, <em>cergurine</em>, <em>grusht shteti</em>, <em>bymyen</em></td></tr>
<tr><td>Hindi</td><td><em>सत्याग्रह</em>, <em>हिस्सेदारी</em>, <em>नक़लची</em>, <em>मोती</em>, <em>धनुर्विद्या</em>, <em>मुक्का</em>, <em>मार्मिक</em>, <em>प्रतिभाव
ान</em>, <em>नियमित</em>, <em>प्रासंगिकता</em>, <em>कीकर</em>, <em>पुष्पांजलि</em>, <em>जोन्ह</em>, <em>याचक</em>, <em>निकट</em>, <em>अकाल</em>, <em>मुँहतोड़</em>, 
<em>मूलकण</em>, <em>धर्मशाला</em>, <em>म्याऊँ</em>, <em>दिक्पात</em>, <em>कचनार</em>, <em>पद्मिनी</em>, <em>छिन</em>, <em>क्रम</em></td><td><em>समधियो</em>, <em>मिल
वानी</em>, <em>अंधियारा</em>, <em>भरी</em>, <em>पलटवाती</em>, <em>समझाते</em>, <em>चोरों</em>, <em>काटे</em>, <em>के कारण</em>, <em>वरदानों</em>, <em>दान देना</em>,
 <em>कुरेदनेवाली</em>, <em>मस्तिष्क स्तम्भ</em>, <em>घटेंगे</em>, <em>डायन</em>, <em>पछाड़ेगी</em>, <em>जमघट्ट</em>, <em>प्रतियो</em>, <em>खरीदोगे</em>, <em>समझता</em>, <em>वेधशालाएँ</em>, <em>ख़ुशबुओं</em>, <em>गलतियों</em>, <em>मर्दो</em>, <em>बाटेंगी</em></td></tr>
<tr><td>Persian</td><td><em>دخل</em>, <em>نوچ</em>, <em>بهت</em>, <em>قلیان</em>, <em>لفاف</em>, <em>ناکام</em>, <em>دوازده‌امامی</em>, <em>تغییر</em>, <em>آدمیت</e
m>, <em>وحشت</em>, <em>واردات</em>, <em>ساماندهی</em>, <em>بهاری</em>, <em>جلاد</em>, <em>اله</em>, <em>عزیمت</em>, <em>انبازی</em>, <em>کبودی</em>, <em>یبوست</em>,
 <em>مواجه</em>, <em>گنده</em>, <em>آذوقه</em>, <em>تقلیل</em>, <em>زهرشناسی</em>, <em>موزه</em></td><td><em>مجبور کردن</em>, <em>دان</em>, <em>بهادر</em>, <em>پرک<
/em>, <em>جوش</em>, <em>می‌دیدم</em>, <em>گابن</em>, <em>مجروح کردن</em>, <em>ارشاد</em>, <em>اوت</em>, <em>میکروـ</em>, <em>جمهوری دموکراتیک کنگو</em>, <em>عقب‌افت
اده</em>, <em>اعضا</em>, <em>کشتی گرفتن</em>, <em>هفته‌ها</em>, <em>جمهوری دموکراتیک افغانستان</em>, <em>خزنده</em>, <em>سوق دادن</em>, <em>بد اخلاق</em>, <em>پس فردا</em>, <em>شکل گرفتن</em>, <em>مدیریت داده‌ها</em>, <em>می‌نوشد</em>, <em>گران‌تر</em></td></tr>
<tr><td>Georgian</td><td><em>შორსმხედველი</em>, <em>დრენაჟი</em>, <em>სულთანი</em>, <em>ფიწიღი</em>, <em>წინამძღვარი</em>, <em>ნახევარკუნძულოვანი</em>, <em>ბაქტერია
</em>, <em>ნატურალიზაცია</em>, <em>მისცემს</em>, <em>იუსტიცია</em>, <em>ძიძიშვილი</em>, <em>აბლაკი</em>, <em>შემოდგომა</em>, <em>ილოტი</em>, <em>ხალიფა</em>, <em>და
უბეგრავი</em>, <em>დანდალუკი</em>, <em>ცუნამი</em>, <em>თელვადი</em>, <em>ბუდობა</em>, <em>ნაძლევი</em>, <em>ფეხსაცმელი</em>, <em>სოციალიზმი</em>, <em>მეტაფორული</e
m>, <em>პოლიმორფული</em></td><td><em>ჯენიფერი</em>, <em>სიყვარულო</em>, <em>ბრიტანეთი</em>, <em>განადგურების</em>, <em>მემარჯვენე პოპულიზმი</em>, <em>კავები</em>, <
em>ვეტოს დადება</em>, <em>ითვლებოდა</em>, <em>წინა აზია</em>, <em>შემოდგომა</em>, <em>დარდანელის სრუტე</em>, <em>-ზე</em>, <em>საჯარო მოხელე</em>, <em>უძლეველი არმა
და</em>, <em>ასაქცევი</em>, <em>ქიმიური ფიზიკა</em>, <em>ჭიის ხვრელი</em>, <em>კონტინენტური ევროპის სამართალი</em>, <em>გონების თვალი</em>, <em>ლოყები</em>, <em>თავდაპირველი სამშობლო</em>, <em>ფლამანდური</em>, <em>ბრაბანტი</em>, <em>ფარდობითობის ზოგადი თეორია</em>, <em>გერმანიის ფედერაციული რესპუბლიკა</em></td></tr>
<tr><td>Finnish</td><td><em>viilipytty</em>, <em>karkaaminen</em>, <em>lennättää</em>, <em>filmata</em>, <em>pensseli</em>, <em>kannustaa</em>, <em>elinkaari</em>, 
<em>vesirakentaminen</em>, <em>tuulitunneli</em>, <em>metropoli</em>, <em>pääepäilty</em>, <em>miä</em>, <em>sääasema</em>, <em>surffaus</em>, <em>pelitapa</em>, <e
m>lihaliemi</em>, <em>ventovieras</em>, <em>epämääräinen</em>, <em>pistelasku</em>, <em>hanuri</em>, <em>lapsiporno</em>, <em>harkita</em>, <em>ranneketju</em>, <em
>jyystää</em>, <em>kuningataräiti</em></td><td><em>dumpperi</em>, <em>kyttyräselkä</em>, <em>mandariinit</em>, <em>toissakesäinen</em>, <em>kuljetuskustannus</em>, 
<em>ihomato</em>, <em>keittosyvennys</em>, <em>kesänä</em>, <em>kääpiökiipijähiiri</em>, <em>informaatiopolitiikka</em>, <em>rahkasuo</em>, <em>hammastua</em>, <em>
harmaansininen</em>, <em>keltainen 2G</em>, <em>sopusoinnussa</em>, <em>puhallella</em>, <em>aavikoituisivat</em>, <em>risteilyt</em>, <em>käyttöihin</em>, <em>ruutuseiska</em>, <em>piitimensaame</em>, <em>riipan</em>, <em>betonirakenne</em>, <em>tuplapenetraatio</em>, <em>kelmiä</em></td></tr>
<tr><td>Turkish</td><td><em>sik</em>, <em>kucak</em>, <em>tükürmek</em>, <em>hoşaf</em>, <em>kanlarınızın</em>, <em>esinlemek</em>, <em>kiremit</em>, <em>sülfür</em
>, <em>ancak</em>, <em>yeröte</em>, <em>altrüist</em>, <em>derleme</em>, <em>haşa</em>, <em>kerpeten</em>, <em>imkân</em>, <em>adaylık</em>, <em>spekülatif</em>, <e
m>baget</em>, <em>abartmacı</em>, <em>meşruiyet</em>, <em>bro</em>, <em>farik</em>, <em>yeğ</em>, <em>sattırtmak</em>, <em>müjde</em></td><td><em>katma</em>, <em>pe
rmütasyonu</em>, <em>Larissa</em>, <em>voleybolu</em>, <em>fizikçiler</em>, <em>alaca doğan</em>, <em>bahis oynamak</em>, <em>duyu-dil programlamayı</em>, <em>İnan<
/em>, <em>canavarların</em>, <em>yorganın</em>, <em>gaz odası</em>, <em>uyurum</em>, <em>başını</em>, <em>Alaca</em>, <em>kat'î</em>, <em>çıraklara</em>, <em>kralla
rın</em>, <em>Yenifakılı</em>, <em>ziyaretçiler</em>, <em>yordamın</em>, <em>yardım etmek</em>, <em>şalgam dolması</em>, <em>peygamberler</em>, <em>Gölpazarı</em></td></tr>
<tr><td>Korean</td><td><em>보급</em>, <em>통거미</em>, <em>와전</em>, <em>그룹</em>, <em>산후통</em>, <em>시력</em>, <em>글래머</em>, <em>사암</em>, <em>압생트</em>
, <em>좆대가리</em>, <em>정맥</em>, <em>야레</em>, <em>클릭</em>, <em>스카</em>, <em>환경</em>, <em>전통적</em>, <em>말대꾸하다</em>, <em>빛깔</em>, <em>꿀벌</em>, 
<em>보리수</em>, <em>어드럭하다</em>, <em>이탈리아어</em>, <em>만발하다</em>, <em>빨딱</em>, <em>공주님</em></td><td><em>안후이</em>, <em>철산</em>, <em>겨울 스포츠
/em>, <em>지난</em>, <em>쏘비에트 사회주의 공화국 련방</em>, <em>배타적 경제 수역</em>, <em>우즈베끼스딴</em>, <em>가새다</em>, <em>토이기</em>, <em>파키스탄</em>,,
 <em>X레이</em>, <em>저울자리</em>, <em>가매</em>, <em>-도</em>, <em>라아단</em>, <em>-케</em>, <em>무스거</em>, <em>페로 제도</em>, <em>주체사상</em>, <em>비타민 D2</em>, <em>둘-</em>, <em>시디 플레이어</em>, <em>랭면</em>, <em>게이 프라이드</em>, <em>오호</em></td></tr>
<tr><td>Indonesian</td><td><em>pemantapan</em>, <em>menyelesaikan</em>, <em>petahana</em>, <em>siang</em>, <em>kereb</em>, <em>tabuh</em>, <em>ragu</em>, <em>cabai<
/em>, <em>arsenik</em>, <em>keserasian</em>, <em>kanca</em>, <em>reaksi</em>, <em>cemen</em>, <em>dulur</em>, <em>meni</em>, <em>katalis</em>, <em>bilas</em>, <em>g
eulis</em>, <em>birama</em>, <em>barut</em>, <em>penghindaran</em>, <em>wirausaha</em>, <em>mengoperasi</em>, <em>magersari</em>, <em>kapasitansi</em></td><td><em>s
etor muka</em>, <em>densitas mineral tulang</em>, <em>galat absolut</em>, <em>saluran pelanggan</em>, <em>waktu paruh</em>, <em>peta situs</em>, <em>dikosongkan</em
>, <em>beda tipis</em>, <em>sakramen rekonsiliasi</em>, <em>kaidah hukum</em>, <em>kehidupan nyata</em>, <em>sel udara</em>, <em>Prapaskah</em>, <em>yuks</em>, <em>
abu gosok</em>, <em>meng-</em>, <em>metode penyusutan</em>, <em>mee</em>, <em>tata graha</em>, <em>Gumelar</em>, <em>saluran induk</em>, <em>tahun ajaran</em>, <em>tulung</em>, <em>yuri</em>, <em>guru pamong</em></td></tr>
<tr><td>Malay</td><td><em>akuarium</em>, <em>forsep</em>, <em>sok</em>, <em>kemabukan</em>, <em>liang</em>, <em>batas</em>, <em>ekadasa</em>, <em>meleis</em>, <em>k
antor</em>, <em>tabib</em>, <em>yuyu</em>, <em>salji</em>, <em>politikus</em>, <em>sepatu</em>, <em>jajahan</em>, <em>tengkujuh</em>, <em>seroja</em>, <em>ovari</em
>, <em>tuanku</em>, <em>penggawa</em>, <em>animasi</em>, <em>bawal</em>, <em>tahil</em>, <em>tatabahasa</em>, <em>maun</em></td><td><em>putra</em>, <em>Bachok</em>,
 <em>sektor awam</em>, <em>enam likur</em>, <em>asam garam</em>, <em>keselamatan siber</em>, <em>maklum balas</em>, <em>limau bali</em>, <em>cicit laki-laki</em>, <
em>jenis darah</em>, <em>oneng-oneng laki-laki</em>, <em>samun gurun</em>, <em>bilik rehat</em>, <em>anat</em>, <em>limă</em>, <em>ayam-ayam</em>, <em>Negara Brunei
 Darussalam</em>, <em>Sep</em>, <em>hormat senjata</em>, <em>Wasap</em>, <em>Nov</em>, <em>batu kawi</em>, <em>sebiru</em>, <em>slip gaji</em>, <em>kelemari</em></td></tr>
<tr><td>Arabic</td><td><em>ابتلعي</em>, <em>انمين</em>, <em>جزى</em>, <em>يبتدئن</em>, <em>تفطرتن</em>, <em>يؤمن</em>, <em>حضروا</em>, <em>نيتروجين</em>, <em>مركيزة
</em>, <em>تعتقدن</em>, <em>أتخذ</em>, <em>قردتم</em>, <em>أسخطتن</em>, <em>تحسبن</em>, <em>استدررت</em>, <em>ردفت</em>, <em>عاق</em>, <em>أخرنطم</em>, <em>يهاجم</e
m>, <em>يتزلزلون</em>, <em>أديت</em>, <em>خطمن</em>, <em>بطة</em>, <em>يهجمن</em>, <em>تستنرن</em></td><td><em>لوحات مفاتيح</em>, <em>أوكلاهوما</em>, <em>الصويرة</e
m>, <em>مدين</em>, <em>سلوك</em>, <em>إشعار</em>, <em>منتف</em>, <em>هفو</em>, <em>رأسمالية</em>, <em>هندسة معمارية</em>, <em>فغر</em>, <em>مداخلة</em>, <em>إفريقيا
</em>, <em>بقجة</em>, <em>خفر</em>, <em>تأدية</em>, <em>تجر</em>, <em>جهارمحال وبختياري</em>, <em>بكين</em>, <em>صفي الدين</em>, <em>مقاولة</em>, <em>الامرأت</em>, <em>تكدس</em>, <em>تعال</em>, <em>الدنمرك</em></td></tr>
<tr><td>Swahili</td><td><em>mfano</em>, <em>kifafa</em>, <em>mwanachuoni</em>, <em>rejea</em>, <em>pasa</em>, <em>hadubini</em>, <em>moshogi</em>, <em>furahi</em>, 
<em>chapati</em>, <em>puliza</em>, <em>bodi</em>, <em>kupatwa</em>, <em>ubadhirifu</em>, <em>sijui</em>, <em>ustawishaji</em>, <em>uenezaji</em>, <em>jemadari</em>,
 <em>ala</em>, <em>mkabidhi</em>, <em>mafundisho</em>, <em>motisha</em>, <em>dira</em>, <em>shuke</em>, <em>pasipoti</em>, <em>azimio</em></td><td><em>zaliana</em>,
 <em>wanajibu</em>, <em>misumeno ya mnyororo</em>, <em>Yoeli</em>, <em>watunza</em>, <em>nyongwa</em>, <em>kusafihi</em>, <em>magruneti</em>, <em>kufurika</em>, <em
>kukerana</em>, <em>telekea</em>, <em>kupendwa</em>, <em>huko</em>, <em>wenza</em>, <em>mikorogo</em>, <em>shushika</em>, <em>vizuizui</em>, <em>tunarudi</em>, <em>chomeka</em>, <em>utotoni</em>, <em>kubakisha</em>, <em>kuinuza</em>, <em>ugonjwa wa kupooza</em>, <em>kusambaratisha</em>, <em>themanini na mbili</em></td></tr>   
</table>
