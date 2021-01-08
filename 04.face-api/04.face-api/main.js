$(document).ready(function () {
    //do something
    $("#thisButton").click(function () {
        processImage();
    });
});

function processImage() {

    $("#picDescription").empty();

    //確認區域與所選擇的相同，因為使用免費的，所以區域選West Center US
    var uriBase = "https://southcentralus.api.cognitive.microsoft.com/face/v1.0/detect";

    var params = {
        "returnFaceId": "true",
        "returnFaceLandmarks": "false",
        "returnFaceAttributes":
            "age,gender,headPose,smile,facialHair,glasses,emotion," +
            "hair,makeup,occlusion,accessories,blur,exposure,noise"
    };
    //顯示分析的圖片
    var sourceImageUrl = document.getElementById("inputImage").value;
    document.querySelector("#sourceImage").src = sourceImageUrl;
    //送出分析
    $.ajax({
        url: uriBase + "?" + $.param(params),
        // Request header
        beforeSend: function (xhrObj) {
            xhrObj.setRequestHeader("Content-Type", "application/json");
            xhrObj.setRequestHeader("Ocp-Apim-Subscription-Key", subscriptionKey);
        },
        type: "POST",
        // Request body
        data: '{"url": ' + '"' + sourceImageUrl + '"}',
    })
        .done(function (data) {
            //顯示JSON內容
            $("#responseTextArea").val(JSON.stringify(data, null, 2));

            for (let x = 0; x < data.length; x++) {
                let thisAccessories = data[x].faceAttributes.accessories;
                if (thisAccessories.length > 0) {
                    let hasMask = false;
                    for (let y = 0; y < thisAccessories.length; y++) {
                        if (thisAccessories[y].type == "mask" && thisAccessories[y].confidence >= 0.7) {
                            hasMask = true;
                        }
                    }
                    if (hasMask) {
                        $("#picDescription").append("V");
                    }
                    else {
                        $("#picDescription").append("X");
                    }
                }
                else {
                    $("#picDescription").append("X");
                }
            }
        })
        .fail(function (jqXHR, textStatus, errorThrown) {
            //丟出錯誤訊息
            var errorString = (errorThrown === "") ? "Error. " : errorThrown + " (" + jqXHR.status + "): ";
            errorString += (jqXHR.responseText === "") ? "" : jQuery.parseJSON(jqXHR.responseText).message;
            alert(errorString);
        });
};