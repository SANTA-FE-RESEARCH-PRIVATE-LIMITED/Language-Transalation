get_language_code = async () => {
    const response = await fetch("http://127.0.0.1:8400/language_code")
    return await response.json()
}

transliterate = async (payload) => {
    try {
        response = await fetch('http://127.0.0.1:8400/tranliterate', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });
    }
    catch (err) {
        console.log(err)
    }
    return await response.json()
}

triggered = async (e) => {
    sentence = document.querySelector("#transition_from").value
    from_lang = document.querySelector("select[name='from']").value
    to_lang = document.querySelector("select[name='to']").value
    payload = {
        "from_language": from_lang,
        "to_language": to_lang,
        "sentence": sentence
    }
    response = await transliterate(payload)
    translitered_box = document.querySelector("#transition_to")
    translitered_box.value = response["translitered"]
}

(async () => {
    languages = await get_language_code()
    languages = languages.sort()
    select_element = document.querySelectorAll("#available_languages")
    select_element.forEach(element => {
        languages.forEach(language => {
            if (element.name == "to" && language == "autodetect") {
                return
            }
            var opt = document.createElement('option');
            if (language == "autodetect") {
                console.log("Triggered")
                opt.selected = "selected"
                console.log(element)
            }
            opt.value = language;
            opt.innerHTML = language;
            element.appendChild(opt);
        })
    })
})()