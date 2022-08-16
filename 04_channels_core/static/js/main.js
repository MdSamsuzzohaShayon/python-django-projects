$(document).ready(function () {
  $("#progress-bar").progress();
});

const progressLabel = document.querySelector(".label");
const progressBar = document.getElementById("progress-bar");

// console.log({progressBar});
progressBar.dataset.percent = '80';

const ws_url = `ws://localhost:8000/ws/new/`;
const socket = new WebSocket(ws_url);

socket.onopen = function (e) {
  console.log("Socket connected");
};

socket.onmessage = function (e) {
  const data = JSON.parse(e.data);
  // console.log(data);
  if (data.payload) {
    if (data.payload.student_name) {
      // progressBar.dataset.percent = (data.payload.current_total * 100) / data.payload.total;
      console.log(
        "Percent - " + (data.payload.current_total * 100) / data.payload.total
      );
      addData(data.payload);
    }
  }
};

socket.onclose = function (e) {
  console.log("Socket disconnected");
};

function addData(data) {
  const html = `
  <tr>
    <td data-label="ID">${data.current_total}</td>
    <td data-label="Name">${data.student_name}</td>
    <td data-label="Age">${data.student_age}</td>
    <td data-label="Address">${data.student_address}</td>
  </tr>
  `;

  document.querySelector("#table-data").innerHTML += html;
}
