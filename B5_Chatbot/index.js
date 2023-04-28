function init() {
  let res_elm = document.createElement("div");
  res_elm.innerHTML = "Hello Myself AlTron, How can I help you?";
  res_elm.setAttribute("class", "left");

  document.getElementById("msg").appendChild(res_elm);
}

let enterFunctionality = (async (e) => {
  e.preventDefault();

  var req = document.getElementById("msg_send").value;

  if (req == undefined || req == "") {
  } else {
    var res = "";
    await axios
      .get(`http://127.0.0.1:5002/bot?message=${req}`)
      .then((data) => {
        console.log(data);
        res = JSON.stringify(data.data.message).replace(/"/g,"");
      });
    
    let data_req = document.createElement("div");
    let data_res = document.createElement("div");

    let container1 = document.createElement("div");
    let container2 = document.createElement("div");

    container1.setAttribute("class", "msgCon1");
    container2.setAttribute("class", "msgCon2");

    data_req.innerHTML = req;
    data_res.innerHTML = res;

    data_req.setAttribute("class", "right");
    data_res.setAttribute("class", "left");

    let message = document.getElementById("msg");

    message.appendChild(container1);
    message.appendChild(container2);

    container1.appendChild(data_req);
    container2.appendChild(data_res);

    document.getElementById("msg_send").value = "";

    function scroll() {
      var scrollMsg = document.getElementById("msg");
      scrollMsg.scrollTop = scrollMsg.scrollHeight;
    }
    scroll();
  }
});

// Enter functionality for send button
document.addEventListener("keydown", async (e) => {
  if (e.key === 'Enter') {
    enterFunctionality(e);
  }
  if(e.key === "/")
  {
    let inputbar = document.querySelector("#msg_send");
    e.preventDefault();
    inputbar.focus();
    
  }
})
// Click functionality for send button
document.getElementById("reply").addEventListener("click", async (e) => {

  enterFunctionality(e);


});



