# soaper-ketsu
I'll update this probably once a month incase soaper breaks and i need to change it to the next soap2ay clone.

If you wanna make the code more readable, feel free to submit a PR but I don't plan on making the code prettier.

{
    "moduleInfo": {
        "moduleName": "ReadComicOnline",
        "moduleInitials": "RCO",
        "moduleDesc": "Read comics",
        "developer": "Jack_",
        "moduleID": "4Rd2dFvYSzf",
        "moduleImage": "https://i.imgur.com/UXQ0Wn2.png",
        "moduleVersion": 1.9,
        "moduleLenguage": "ENG",
        "moduleType": "Image",
        "baseURL": "https://readcomiconline.li/",
        "moduleDeveloperSite": "https://cyborg714.github.io/ketsu/",
        "UpdateSite": "https://raw.githubusercontent.com/Cyborg714/ketsu/main/image/readcomiconline.json",
        "preferedServer": "",
        "preferedDownloadServer": "",
        "blackListed": [
            ""
        ]
    },
    "global": {
        "variables": [
            {
                "key": "",
                "value": ""
            }
        ],
        "cookies": [
            {
                "key": "",
                "value": ""
            }
        ],
        "headers": [
            {
                "key": "",
                "value": ""
            }
        ]
    },
    "mainPage": [
        {
            "request": {
                "url": "https://readcomiconline.li/",
                "method": "get",
                "headers": [
                    {
                        "key": "",
                        "value": ""
                    }
                ],
                "httpBody": null
            },
            "extra": {
                "commands": [
                    {
                        "commandName": "",
                        "params": [
                            {
                                "key": "",
                                "value": ""
                            }
                        ]
                    }
                ],
                "extraInfo": [
                    {
                        "key": "",
                        "value": ""
                    }
                ]
            },
            "javascriptConfig": {
                "removeJavascript": true,
                "loadInWebView": false,
                "javaScript": "const DefaultLayouts = { ultraWideFull: 'ultraWideFull', ultraWide: 'ultraWide', wideFull: 'wideFull', wide: 'wide', wideStrechedFull: 'wideStrechedFull', wideStrechedFullDouble: 'WideStrechedFullDouble', wideStreched: 'wideStreched', wideStrechedDouble: 'wideStrechedDouble', wideStrechedFullList: 'wideStrechedFullList', wideStrechedList: 'wideStrechedList', doublets: 'doublets', doubletsDouble: 'doubletsDouble', doubletsFull: 'doubletsFull', doubletsFullDouble: 'doubletsFullDouble', doubletsConstant: 'doubletsConstant', doubletsDoubleConstant: 'doubletsDoubleConstant', doubletsFullConstant: 'doubletsFullConstant', doubletsFullDoubleConstant: 'doubletsFullDoubleConstant', longDoublets: 'longDoublets', longDoubletsDouble: 'longDoubletsDouble', longDoubletsFull: 'longDoubletsFull', longDoubletsFullDouble: 'longDoubletsFullDouble', longDoubletsConstant: 'longDoubletsConstant', longDoubletsDoubleConstant: 'longDoubletsDoubleConstant', longDoubletsFullConstant: 'longDoubletsFullConstant', longDoubletsFullDoubleConstant: 'longDoubletsFullDoubleConstant', triplets: 'triplets', tripletsDouble: 'tripletsDouble', tripletsFull: 'tripletsFull', tripletsFullDouble: 'tripletsFullDouble', tripletsConstant: 'tripletsConstant', tripletsDoubleConstant: 'tripletsDoubleConstant', tripletsFullConstant: 'tripletsFullConstant', tripletsFullDoubleConstant: 'tripletsFullDoubleConstant', longTriplets: 'longTriplets', longTripletsDouble: 'longTripletsDouble', longTripletsFull: 'longTripletsFull', longTripletsFullDouble: 'longTripletsFullDouble', longTripletsConstant: 'longTripletsConstant', longTripletsDoubleConstant: 'longTripletsDoubleConstant', longTripletsFullConstant: 'longTripletsFullConstant', longTripletsFullDoubleConstant: 'longTripletsFullDoubleConstant', none: ''};const CellDesings = { Special1: 'Special1', Special2: 'Special2', Special3: 'Special3', CELLHelperText: 'CELLHelperText', small1: 'small1', small2: 'small2', normal1: 'normal1', normal2: 'normal2', normal3: 'normal3', normal4: 'normal4', normal5: 'normal5', normal6: 'normal6', normal7: 'normal7', wide1: 'wide1', wide2: 'wide2', wide3: 'wide3', wide4: 'wide4', wide5: 'wide5', wide6: 'wide6', wide7: 'wide7', wide8: 'wide8', wide9: 'wide9', wide10: 'wide10', wide11: 'wide11'};const Paging = { leading: 'leading', centered: 'centered', none: ''};const Orientation = { horizontal: 'horizontal', vertical: 'vertical'};function MainPage(request, extra, javascriptConfig, output) { this.request = request; this.extra = extra; this.javascriptConfig = javascriptConfig; this.output = output;}function ModuleRequest(url, method, headers, httpBody) { this.url = url; this.method = method; this.headers = headers; this.httpBody = httpBody;}function Extra(commands, extraInfo) { this.commands = commands; this.extraInfo = extraInfo;}function Commands(commandName, params) { this.commandName = commandName; this.params = params;}function JavascriptConfig(removeJavascript, loadInWebView, javaScript) { this.removeJavascript = removeJavascript; this.loadInWebView = loadInWebView; this.javaScript = javaScript;}function KeyValue(key, value) { this.key = key; this.value = value;}function Output(cellDesing, orientation, defaultLayout, paging, section, layout, data) { this.cellDesing = cellDesing; this.orientation = orientation; this.defaultLayout = defaultLayout; this.paging = paging; this.section = section; this.layout = layout; this.data = data;}function Section(sectionName, separator) { this.sectionName = sectionName; this.separator = separator;}function Layout(insets, visibleCellsWidthS, visibleCellsWidthM, visibleCellsWidthL, visibleCellsHeight, heightForVisibleCells, cellSize, ratio, constant, horizontalSpacing, verticalSpacing) { this.insets = insets; this.visibleCellsWidthS = visibleCellsWidthS; this.visibleCellsWidthM = visibleCellsWidthM; this.visibleCellsWidthL = visibleCellsWidthL; this.visibleCellsHeight = visibleCellsHeight; this.heightForVisibleCells = heightForVisibleCells; this.cellSize = cellSize; this.ratio = ratio; this.constant = constant; this.horizontalSpacing = horizontalSpacing; this.verticalSpacing = verticalSpacing;}function Insets(top, bottom, left, right) { this.top = top; this.bottom = bottom; this.left = left; this.right = right;}function Size(width, height) { this.width = width; this.height = height;}function Ratio(inRelation, number1, number2) { this.inRelation = inRelation; this.number1 = number1; this.number2 = number2;}function Data(image, title, description, field1, field2, field3, field4, isChapter, link, openInWebView) { this.image = image; this.title = title; this.description = description; this.field1 = field1; this.field2 = field2; this.field3 = field3; this.field4 = field4; this.isChapter = isChapter; this.link = link; this.openInWebView = openInWebView;}const savedData = document.getElementById('ketsu-final-data');const parsedJson = JSON.parse(savedData.innerHTML);let output = [];let popular = [];let topNews = [];let latest = [];const emptyKeyValue = [new KeyValue('', '')];const topMost = document.querySelectorAll('#tab-mostview > div');for (const top of topMost) { if (top.querySelector('a').className.includes('red')) continue; let link = top.querySelector('a:not(.title)').href; link = new URL(link, parsedJson.request.url).href; link = new ModuleRequest(link, 'get', emptyKeyValue, null); let image = top.querySelector('a:not(.title) > img').src; image = image.indexOf('/') != 0 ? image : new URL(image, parsedJson.request.url).href; image = new ModuleRequest(image, 'get', emptyKeyValue, null); const title = top.querySelector('a.title > span').textContent.trim(); const obj = new Data(image, title, 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', false, link, false); popular.push(obj);}const topNew = document.querySelectorAll('#tab-newest > div');for (const top of topNew) { if (top.querySelector('a').className.includes('red')) continue; let link = top.querySelector('a:not(.title)').href; link = new URL(link, parsedJson.request.url).href; link = new ModuleRequest(link, 'get', emptyKeyValue, null); let image = top.querySelector('a:not(.title) > img').src; image = image.indexOf('/') != 0 ? image : new URL(image, parsedJson.request.url).href; image = new ModuleRequest(image, 'get', emptyKeyValue, null); const title = top.querySelector('a.title > span').textContent.trim(); const genresArr = top.querySelectorAll('p:first-of-type > a'); let genres = []; for (const genre of genresArr) { genres.push(genre.textContent.trim()) } const obj = new Data(image, title, genres.join(', '), 'unknown', 'unknown', 'unknown', 'unknown', false, link, false); topNews.push(obj);}const latestUp = document.querySelectorAll('.barContent > .scrollable > .items > div > a');for (const top of latestUp) { let link = new URL(top.href, parsedJson.request.url).href; link = new ModuleRequest(link, 'get', emptyKeyValue, null); let image = top.querySelector('img'); image = image.src ? image.src : image.getAttribute('srctemp'); image = image.indexOf('/') != 0 ? image : new URL(image, parsedJson.request.url).href; image = new ModuleRequest(image, 'get', emptyKeyValue, null); const title = top.querySelector('br').nextSibling.textContent.trim(); const obj = new Data(image, title, 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', false, link); latest.push(obj);}output.push(new Output(CellDesings.Special1, Orientation.horizontal, DefaultLayouts.triplets, Paging.leading, new Section('Most popular', true), null, popular));output.push(new Output(CellDesings.wide9, Orientation.horizontal, DefaultLayouts.wideStrechedList, Paging.leading, new Section('New', true), null, topNews));output.push(new Output(CellDesings.normal4, Orientation.vertical, DefaultLayouts.longTripletsFull, Paging.none, new Section('Latest', true), null, latest));const MainPageObject = new MainPage(new ModuleRequest('', 'get', emptyKeyValue, null), new Extra([new Commands('', emptyKeyValue)], emptyKeyValue), new JavascriptConfig(true, false, ''), output);const finalJson = JSON.stringify(MainPageObject);savedData.innerHTML = finalJson;"
            },
            "output": [
                {
                    "cellDesing": "normal1",
                    "orientation": "vertical",
                    "defaultLayout": "wide",
                    "paging": "",
                    "section": {
                        "sectionName": "",
                        "separator": false
                    },
                    "layout": {
                        "insets": {
                            "top": 0,
                            "bottom": 0,
                            "left": 0,
                            "right": 0
                        },
                        "visibleCellsWidthS": 2,
                        "visibleCellsWidthM": 2,
                        "visibleCellsWidthL": 2,
                        "visibleCellsHeight": 2,
                        "heightForVisibleCells": 400,
                        "cellSize": {
                            "width": 300,
                            "height": 300
                        },
                        "ratio": {
                            "inRelation": "width",
                            "number1": 1,
                            "number2": 2
                        },
                        "constant": {
                            "width": 1,
                            "height": 2
                        },
                        "horizontalSpacing": 0,
                        "verticalSpacing": 0
                    },
                    "data": [
                        {
                            "image": {
                                "url": "",
                                "method": "get",
                                "headers": [
                                    {
                                        "key": "",
                                        "value": ""
                                    }
                                ],
                                "httpBody": null
                            },
                            "title": "",
                            "description": "",
                            "field1": "",
                            "field2": "",
                            "field3": "",
                            "field4": "",
                            "openInWebView": false,
                            "isChapter": false,
                            "link": {
                                "url": "",
                                "method": "",
                                "headers": [
                                    {
                                        "key": "",
                                        "value": ""
                                    }
                                ],
                                "httpBody": null
                            }
                        }
                    ]
                }
            ]
        }
    ],
    "search": [
        {
            "request": {
                "url": "https://readcomiconline.li/Search/Comic",
                "method": "POST",
                "headers": [
                    {
                        "key": "content-type",
                        "value": "application/x-www-form-urlencoded"
                    },
                    {
                        "key": "Referer",
                        "value": "https://readcomiconline.li/Search/Comic"
                    }
                ],
                "httpBody": "keyword=<searched>"
            },
            "separator": "%20",
            "extra": {
                "commands": [
                    {
                        "commandName": "",
                        "params": [
                            {
                                "key": "",
                                "value": ""
                            }
                        ]
                    }
                ],
                "extraInfo": [
                    {
                        "key": "",
                        "value": ""
                    }
                ]
            },
            "javascriptConfig": {
                "removeJavascript": true,
                "loadInWebView": false,
                "javaScript": "const DefaultLayouts = { ultraWideFull: 'ultraWideFull', ultraWide: 'ultraWide', wideFull: 'wideFull', wide: 'wide', wideStrechedFull: 'wideStrechedFull', wideStrechedFullDouble: 'WideStrechedFullDouble', wideStreched: 'wideStreched', wideStrechedDouble: 'wideStrechedDouble', wideStrechedFullList: 'wideStrechedFullList', wideStrechedList: 'wideStrechedList', doublets: 'doublets', doubletsDouble: 'doubletsDouble', doubletsFull: 'doubletsFull', doubletsFullDouble: 'doubletsFullDouble', doubletsConstant: 'doubletsConstant', doubletsDoubleConstant: 'doubletsDoubleConstant', doubletsFullConstant: 'doubletsFullConstant', doubletsFullDoubleConstant: 'doubletsFullDoubleConstant', longDoublets: 'longDoublets', longDoubletsDouble: 'longDoubletsDouble', longDoubletsFull: 'longDoubletsFull', longDoubletsFullDouble: 'longDoubletsFullDouble', longDoubletsConstant: 'longDoubletsConstant', longDoubletsDoubleConstant: 'longDoubletsDoubleConstant', longDoubletsFullConstant: 'longDoubletsFullConstant', longDoubletsFullDoubleConstant: 'longDoubletsFullDoubleConstant', triplets: 'triplets', tripletsDouble: 'tripletsDouble', tripletsFull: 'tripletsFull', tripletsFullDouble: 'tripletsFullDouble', tripletsConstant: 'tripletsConstant', tripletsDoubleConstant: 'tripletsDoubleConstant', tripletsFullConstant: 'tripletsFullConstant', tripletsFullDoubleConstant: 'tripletsFullDoubleConstant', longTriplets: 'longTriplets', longTripletsDouble: 'longTripletsDouble', longTripletsFull: 'longTripletsFull', longTripletsFullDouble: 'longTripletsFullDouble', longTripletsConstant: 'longTripletsConstant', longTripletsDoubleConstant: 'longTripletsDoubleConstant', longTripletsFullConstant: 'longTripletsFullConstant', longTripletsFullDoubleConstant: 'longTripletsFullDoubleConstant', none: ''};const CellDesings = { Special1: 'Special1', Special2: 'Special2', Special3: 'Special3', CELLHelperText: 'CELLHelperText', small1: 'small1', small2: 'small2', normal1: 'normal1', normal2: 'normal2', normal3: 'normal3', normal4: 'normal4', normal5: 'normal5', normal6: 'normal6', normal7: 'normal7', wide1: 'wide1', wide2: 'wide2', wide3: 'wide3', wide4: 'wide4', wide5: 'wide5', wide6: 'wide6', wide7: 'wide7', wide8: 'wide8', wide9: 'wide9', wide10: 'wide10', wide11: 'wide11'};const Paging = { leading: 'leading', centered: 'centered', none: ''};const Orientation = { horizontal: 'horizontal', vertical: 'vertical'};function Search(request, extra, separator, javascriptConfig, output) { this.request = request; this.extra = extra; this.separator = separator; this.javascriptConfig = javascriptConfig; this.output = output;}function ModuleRequest(url, method, headers, httpBody) { this.url = url; this.method = method; this.headers = headers; this.httpBody = httpBody;}function Extra(commands, extraInfo) { this.commands = commands; this.extraInfo = extraInfo;}function Commands(commandName, params) { this.commandName = commandName; this.params = params;}function JavascriptConfig(removeJavascript, loadInWebView, javaScript) { this.removeJavascript = removeJavascript; this.loadInWebView = loadInWebView; this.javaScript = javaScript;}function KeyValue(key, value) { this.key = key; this.value = value;}function Output(cellDesing, orientation, defaultLayout, paging, section, layout, data) { this.cellDesing = cellDesing; this.orientation = orientation; this.defaultLayout = defaultLayout; this.paging = paging; this.section = section; this.layout = layout; this.data = data;}function Section(sectionName, separator) { this.sectionName = sectionName; this.separator = separator;}function Layout(insets, visibleCellsWidthS, visibleCellsWidthM, visibleCellsWidthL, visibleCellsHeight, heightForVisibleCells, cellSize, ratio, constant, horizontalSpacing, verticalSpacing) { this.insets = insets; this.visibleCellsWidthS = visibleCellsWidthS; this.visibleCellsWidthM = visibleCellsWidthM; this.visibleCellsWidthL = visibleCellsWidthL; this.visibleCellsHeight = visibleCellsHeight; this.heightForVisibleCells = heightForVisibleCells; this.cellSize = cellSize; this.ratio = ratio; this.constant = constant; this.horizontalSpacing = horizontalSpacing; this.verticalSpacing = verticalSpacing;}function Insets(top, bottom, left, right) { this.top = top; this.bottom = bottom; this.left = left; this.right = right;}function Size(width, height) { this.width = width; this.height = height;}function Ratio(inRelation, number1, number2) { this.inRelation = inRelation; this.number1 = number1; this.number2 = number2;}function Data(image, title, description, field1, field2, field3, field4, isChapter, link, openInWebView) { this.image = image; this.title = title; this.description = description; this.field1 = field1; this.field2 = field2; this.field3 = field3; this.field4 = field4; this.isChapter = isChapter; this.link = link; this.openInWebView = openInWebView;}const savedData = document.getElementById('ketsu-final-data');const parsedJson = JSON.parse(savedData.innerHTML);let output = [];let search = [];const emptyKeyValue = [new KeyValue('', '')];const testLayout = new Layout(new Insets(10, 10, 10, 10), 1, 2, 3, 1, 500, new Size(400, 400), new Ratio('width', 4, 11), new Size(0, 0), 10, 10);if (!document.querySelector('a.bigChar')) { const results = document.querySelectorAll('.list-comic > .item'); if (results.length == 0) { const dummyQuest = new ModuleRequest('empty', 'get', emptyKeyValue, null); const infoText = new Data(dummyQuest, 'Not found, try again', '', '', '', '', '', false, dummyQuest, false); output.push(new Output('CELLHelperText', Orientation.vertical, DefaultLayouts.wideFull, Paging.none, new Section('', true), null, [infoText])); } else { for (const result of results) { let link = result.querySelector('a').href; link = new URL(link, parsedJson.request.url).href; link = new ModuleRequest(link, 'get', emptyKeyValue, null); const title = result.querySelector('a > .title').textContent.trim(); let image = result.querySelector('a > img').src; image = image.indexOf('/') != 0 ? image : new URL(image, parsedJson.request.url).href; image = new ModuleRequest(image, 'get', emptyKeyValue, null); const obj = new Data(image, title, '', '', '', '', '', true, link, false); search.push(obj); } output.push(new Output(CellDesings.wide8, Orientation.vertical, DefaultLayouts.none, Paging.none, new Section('', false), testLayout, search)); }} else { let image = document.querySelector('.rightBox > .barContent > div > img').src; image = image.indexOf('/') != 0 ? image : new URL(image, parsedJson.request.url).href; image = new ModuleRequest(image, 'get', emptyKeyValue, null); const info = document.querySelector('.barContent > div'); const ps = info.querySelectorAll('p'); const title = info.querySelector('a.bigChar').textContent.trim(); let link = info.querySelector('a.bigChar').href; link = new URL(link, parsedJson.request.url).href; link = new ModuleRequest(link, 'get', emptyKeyValue, null); let status = 'unknown'; for (const p of ps) { if (p.querySelector('span') == null) continue; const key = p.querySelector('span.info').textContent.trim(); if (key.includes('Status')) { status = p.querySelector('span').nextSibling.textContent.trim(); } } const obj = new Data(image, title, `Status: ${status}`, '', '', '', '', true, link, false); search.push(obj); output.push(new Output(CellDesings.wide8, Orientation.vertical, DefaultLayouts.none, Paging.none, new Section('', false), testLayout, search));}const searchPageObject = new Search(new ModuleRequest('', '', emptyKeyValue, null), new Extra([new Commands('', emptyKeyValue)], emptyKeyValue), '', new JavascriptConfig(true, false, ''), output);const finalJson = JSON.stringify(searchPageObject);savedData.innerHTML = finalJson;"
            },
            "output": [
                {
                    "cellDesing": "normal1",
                    "orientation": "vertical",
                    "defaultLayout": "wide",
                    "paging": "",
                    "section": {
                        "sectionName": "",
                        "separator": false
                    },
                    "layout": {
                        "insets": {
                            "top": 0,
                            "bottom": 0,
                            "left": 0,
                            "right": 0
                        },
                        "visibleCellsWidthS": 2,
                        "visibleCellsWidthM": 2,
                        "visibleCellsWidthL": 2,
                        "visibleCellsHeight": 2,
                        "heightForVisibleCells": 400,
                        "cellSize": {
                            "width": 300,
                            "height": 300
                        },
                        "ratio": {
                            "inRelation": "width",
                            "number1": 1,
                            "number2": 2
                        },
                        "constant": {
                            "width": 1,
                            "height": 2
                        },
                        "horizontalSpacing": 0,
                        "verticalSpacing": 0
                    },
                    "data": [
                        {
                            "image": {
                                "url": "",
                                "method": "get",
                                "headers": [
                                    {
                                        "key": "",
                                        "value": ""
                                    }
                                ],
                                "httpBody": null
                            },
                            "title": "",
                            "description": "",
                            "field1": "",
                            "field2": "",
                            "field3": "",
                            "field4": "",
                            "openInWebView": false,
                            "isChapter": false,
                            "link": {
                                "url": "empty",
                                "method": "get",
                                "headers": [
                                    {
                                        "key": "key",
                                        "value": "value"
                                    }
                                ],
                                "httpBody": null
                            }
                        }
                    ]
                }
            ]
        }
    ],
    "info": [
        {
            "request": {
                "url": "",
                "method": "get",
                "headers": [
                    {
                        "key": "",
                        "value": ""
                    }
                ],
                "httpBody": null
            },
            "extra": {
                "commands": [
                    {
                        "commandName": "",
                        "params": [
                            {
                                "key": "",
                                "value": ""
                            }
                        ]
                    }
                ],
                "extraInfo": [
                    {
                        "key": "",
                        "value": ""
                    }
                ]
            },
            "javascriptConfig": {
                "removeJavascript": true,
                "loadInWebView": false,
                "javaScript": "function Info(request, extra, javascriptConfig, output) { this.request = request; this.extra = extra; this.javascriptConfig = javascriptConfig; this.output = output;}function ModuleRequest(url, method, headers, httpBody) { this.url = url; this.method = method; this.headers = headers; this.httpBody = httpBody;}function Extra(commands, extraInfo) { this.commands = commands; this.extraInfo = extraInfo;}function Commands(commandName, params) { this.commandName = commandName; this.params = params;}function JavascriptConfig(removeJavascript, loadInWebView, javaScript) { this.removeJavascript = removeJavascript; this.loadInWebView = loadInWebView; this.javaScript = javaScript;}function KeyValue(key, value) { this.key = key; this.value = value;}function Chapter(chapName, link, openInWebView) { this.chapName = chapName; this.link = link; this.openInWebView = openInWebView;}function Output(image, title, link, description, genres, field1, field2, field3, field4, chapters) { this.image = image; this.link = link; this.title = title; this.description = description; this.genres = genres; this.field1 = field1; this.field2 = field2; this.field3 = field3; this.field4 = field4; this.chapters = chapters;}var savedData = document.getElementById('ketsu-final-data');var parsedJson = JSON.parse(savedData.innerHTML);let emptyKeyValue = [new KeyValue('', '')];var episodes = [];var type = 'empty';var status = 'Unknown';var genres = [];var desc = '';var title = '';var image = document.querySelector('.rightBox > .barContent > div > img').src;image = image.indexOf('/') != 0 ? image : new URL(image, parsedJson.request.url).href;image = new ModuleRequest(image, 'get', emptyKeyValue, null);const info = document.querySelector('.barContent > div');const ps = info.querySelectorAll('p');title = info.querySelector('a.bigChar').textContent.trim();for (const p of ps) { if (p.querySelector('span') == null) continue; const key = p.querySelector('span.info').textContent.trim(); if (key.includes('Genres')) { const gs = p.querySelectorAll('a.dotUnder'); for (const g of gs) { genres.push(g.textContent.trim()); } } else if (key.includes('Status')) { status = p.querySelector('span').nextSibling.textContent.trim(); let views = p.querySelector('span').nextElementSibling.nextSibling.textContent.trim(); type = `Views: ${views}`; } else if (key.includes('Summary')) { desc = p.nextElementSibling.textContent.trim(); }}const eps = document.querySelectorAll('table.listing > tbody > tr > td > a');for (const ep of eps) { let link = new URL(ep.href, parsedJson.request.url).href + '&quality=hq'; link = new ModuleRequest(link, 'get', emptyKeyValue, null); const chap = ep.textContent.trim().replace(title, '').trim(); episodes.push(new Chapter(chap, link, false));}let infoPageObject = new Info(new ModuleRequest('', '', emptyKeyValue, null), new Extra([new Commands('', emptyKeyValue)], emptyKeyValue), new JavascriptConfig(false, false, ''), new Output(image, title, parsedJson.request, desc, genres, status, 'Comic', type, 'Chaps: ' + episodes.length, episodes.reverse()));var finalJson = JSON.stringify(infoPageObject);savedData.innerHTML = finalJson;"
            },
            "output": {
                "image": {
                    "url": "",
                    "method": "get",
                    "headers": [
                        {
                            "key": "",
                            "value": ""
                        }
                    ],
                    "httpBody": null
                },
                "link": {
                    "url": "",
                    "method": "get",
                    "headers": [
                        {
                            "key": "",
                            "value": ""
                        }
                    ],
                    "httpBody": null
                },
                "title": "",
                "description": "",
                "genres": [
                    ""
                ],
                "field1": "",
                "field2": "",
                "field3": "",
                "field4": "",
                "chapters": [
                    {
                        "chapName": "",
                        "openInWebView": false,
                        "link": {
                            "url": "empty",
                            "method": "get",
                            "headers": [
                                {
                                    "key": "key",
                                    "value": "value"
                                }
                            ],
                            "httpBody": null
                        }
                    }
                ]
            }
        }
    ],
    "chapters": [
        {
            "request": {
                "url": "",
                "method": "get",
                "headers": [
                    {
                        "key": "key",
                        "value": "value"
                    }
                ],
                "httpBody": null
            },
            "extra": {
                "commands": [
                    {
                        "commandName": "",
                        "params": [
                            {
                                "key": "",
                                "value": ""
                            }
                        ]
                    }
                ],
                "extraInfo": [
                    {
                        "key": "",
                        "value": ""
                    }
                ]
            },
            "javascriptConfig": {
                "removeJavascript": true,
                "loadInWebView": false,
                "javaScript": "function Chapters(request, extra, javascriptConfig, output) { this.request = request; this.extra = extra; this.javascriptConfig = javascriptConfig; this.output = output;}function ModuleRequest(url, method, headers, httpBody) { this.url = url; this.method = method; this.headers = headers; this.httpBody = httpBody;}function Extra(commands, extraInfo) { this.commands = commands; this.extraInfo = extraInfo;}function Commands(commandName, params) { this.commandName = commandName; this.params = params;}function JavascriptConfig(removeJavascript, loadInWebView, javaScript) { this.removeJavascript = removeJavascript; this.loadInWebView = loadInWebView; this.javaScript = javaScript;}function KeyValue(key, value) { this.key = key; this.value = value;}function Output(videos, images, text) { this.videos = videos; this.images = images; this.text = text;}function Videos(needsResolver, rawVideo) { this.needsResolver = needsResolver; this.rawVideo = rawVideo;}function NeedsResolver(resolverIdentifier, link) { this.resolverIdentifier = resolverIdentifier; this.link = link;}function RawVideo(video) { this.video = video;}function Video(videoQuality, videoLink) { this.videoQuality = videoQuality; this.videoLink = videoLink;}function Text(text) { this.text = text;}var output = [];var savedData = document.getElementById('ketsu-final-data');var parsedJson = JSON.parse(savedData.innerHTML);var emptyKeyValue = [new KeyValue('Referer', parsedJson.request.url)];const body = document.querySelector('body').innerHTML;const matches = body.match(/lstImages\\.push\\('([^']+)/g);function beau(image) { let img = image; img = img.replace(/_x236/g, 'd').replace(/_x945/g, 'g'); if (img.indexOf('https') != 0) { let x = img.substring(img.indexOf('?')); img.indexOf('=s0?') > 0 ? img = img.substring(0, img.indexOf('=s0?')) : img = img.substring(0, img.indexOf('=s1600?')); img = img.substring(4, 22) + img.substring(25); img = img.substring(0, img.length - 6) + img[img.length - 2] + img[img.length - 1]; img = decodeURIComponent(escape(atob(img))); img = img.substring(0, 13) + img.substring(17); image.indexOf('=s0') > 0 ? img = img.substring(0, img.length - 2) + '=s0' : img = img.substring(0, img.length - 2) + '=s1600'; img = img + x; return 'https://2.bp.blogspot.com/' + img; } return img;}if (matches) { for (const match of matches) { let image = match.replace('lstImages.push(\\'', ''); image = new ModuleRequest(beau(image), 'get', emptyKeyValue, null); output.push(image); }} else { output.push(new ModuleRequest('https://d1fdloi71mui9q.cloudfront.net/1JBIg7XxQ3WqZ8AAZPiz_GydL9KJ3v5AKUN1B', 'get', emptyKeyValue, null));}let emptyExtra = new Extra([new Commands('', emptyKeyValue)], emptyKeyValue);var chaptersObject = new Chapters(new ModuleRequest('', '', emptyKeyValue, null), emptyExtra, new JavascriptConfig(false, false, ''), new Output(null, output, null));var finalJson = JSON.stringify(chaptersObject);savedData.innerHTML = finalJson;"
            },
            "output": {
                "videos": {
                    "needsResolver": [
                        {
                            "resolverIdentifier": "",
                            "link": {
                                "url": "",
                                "method": "get",
                                "headers": [
                                    {
                                        "key": "key",
                                        "value": "value"
                                    }
                                ],
                                "httpBody": null
                            }
                        }
                    ],
                    "rawVideo": [
                        {
                            "video": [
                                {
                                    "videoQuality": "",
                                    "videoLink": {
                                        "url": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
                                        "method": "get",
                                        "headers": [
                                            {
                                                "key": "key",
                                                "value": "value"
                                            }
                                        ],
                                        "httpBody": null
                                    }
                                }
                            ]
                        }
                    ]
                },
                "images": [
                    {
                        "url": "empty",
                        "method": "get",
                        "headers": [
                            {
                                "key": "key",
                                "value": "value"
                            }
                        ],
                        "httpBody": null
                    }
                ],
                "text": {
                    "text": ""
                }
            }
        }
    ],
    "moduleResolvers": [
        {
            "resolverInfo": {
                "resolverName": "",
                "nameMatches": [
                    ""
                ],
                "developer": "",
                "moduleID": "",
                "resolverVersion": 1,
                "baseURL": ""
            },
            "resolver": [
                {
                    "request": {
                        "url": "",
                        "method": "get",
                        "headers": [
                            {
                                "key": "key",
                                "value": "value"
                            }
                        ],
                        "httpBody": null
                    },
                    "extra": {
                        "commands": [
                            {
                                "commandName": "",
                                "params": [
                                    {
                                        "key": "",
                                        "value": ""
                                    }
                                ]
                            }
                        ],
                        "extraInfo": [
                            {
                                "key": "",
                                "value": ""
                            }
                        ]
                    },
                    "javascriptConfig": {
                        "removeJavascript": false,
                        "loadInWebView": false,
                        "javaScript": ""
                    },
                    "output": {
                        "moduleID": "",
                        "video": [
                            {
                                "videoQuality": "720",
                                "videoLink": {
                                    "url": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
                                    "method": "get",
                                    "headers": [
                                        {
                                            "key": "key",
                                            "value": "value"
                                        }
                                    ],
                                    "httpBody": null
                                }
                            }
                        ]
                    }
                }
            ]
        }
    ],
    "responseCodeFunctions": [
        {
            "code": 0,
            "msgTitle": "",
            "msgBody": "",
            "type": "normal",
            "functions": [
                {
                    "request": {
                        "url": "empty",
                        "method": "get",
                        "headers": [
                            {
                                "key": "key",
                                "value": "value"
                            }
                        ],
                        "httpBody": null
                    },
                    "extra": {
                        "commands": [
                            {
                                "commandName": "",
                                "params": [
                                    {
                                        "key": "",
                                        "value": ""
                                    }
                                ]
                            }
                        ],
                        "extraInfo": [
                            {
                                "key": "",
                                "value": ""
                            }
                        ]
                    },
                    "javascriptConfig": {
                        "removeJavascript": true,
                        "loadInWebView": false,
                        "javaScript": ""
                    }
                }
            ]
        }
    ],
    "helperFunctions": [
        {
            "functionName": "example",
            "msgTitle": "",
            "msgBody": "",
            "type": "normal",
            "functions": [
                {
                    "request": {
                        "url": "empty",
                        "method": "get",
                        "headers": [
                            {
                                "key": "key",
                                "value": "value"
                            }
                        ],
                        "httpBody": null
                    },
                    "extra": {
                        "commands": [
                            {
                                "commandName": "",
                                "params": [
                                    {
                                        "key": "",
                                        "value": ""
                                    }
                                ]
                            }
                        ],
                        "extraInfo": [
                            {
                                "key": "",
                                "value": ""
                            }
                        ]
                    },
                    "javascriptConfig": {
                        "removeJavascript": true,
                        "loadInWebView": false,
                        "javaScript": ""
                    }
                }
            ]
        }
    ]
}