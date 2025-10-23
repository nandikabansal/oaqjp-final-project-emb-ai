let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            // The server returns JSON, so parse it first
            let responseJson = JSON.parse(xhttp.responseText);
            // Assuming the server sends {"result": "...formatted string..."}
            document.getElementById("system_response").innerHTML = responseJson.result;
        }
    };
    
    xhttp.open("POST", "emotionDetector", true);
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhttp.send(JSON.stringify({ text: textToAnalyze }));
}
