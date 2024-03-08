function inputChanged(event) {
    fetch('/sum?n=' + event.target.value )
        .then(response => response.json())
        .then(data => {
            console.log(data);
            document.getElementById("result").value =
                 "Words: " + data["words"] +
                ", Characters: " + data["characters"] + 
                ", Numbers: " + data["numbers"] +
                ", Punctuations: " + data["punctuations"];
        });
}

