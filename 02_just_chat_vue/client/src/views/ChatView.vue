<template>
  <!--    CHAT START -->
  <div class="ui grid chat-wrapper">
    <!--        LEFT START -->
    <div class="four wide column left-side">
      <div class="ui vertical menu left-side-menu">
        <a class="active teal item">
          Inbox
          <div class="ui teal left pointing label">1</div>
        </a>
        <a class="item">
          Spam
          <div class="ui label">51</div>
        </a>
        <a class="item">
          Updates
          <div class="ui label">1</div>
        </a>
        <div class="item">
          <div class="ui transparent icon input">
            <input type="text" placeholder="Search mail..." />
            <i class="search icon"></i>
          </div>
        </div>
      </div>
    </div>
    <!--        LEFT ENDS -->

    <!--        RIGHT START -->
    <div class="twelve wide column right-side">
      <div class="ui teal segment">
        <h4 class="username"></h4>
      </div>
      <!--            SENDER -->

      <div class="ui grid message-grid"></div>

      <br /><br />
      <div class="ui action input input-container">
        <input type="text" class="input-box" placeholder="Send a message" />
        <button class="ui green right labeled icon button submit-btn">
          <i class="paper plane icon"></i>
          Send
        </button>
      </div>

      <!--            RECEIVER-->
    </div>
    <!--        RIGHT ENDS -->
  </div>
  <!--CHAT ENDS -->
</template>


<script>
import WebSocketInstance from "../utils/websocket.js";
import { ref, reactive, onMounted } from "vue";

export default {
  setup() {
    const state = reactive({});

    onMounted(() => {});

    function waitForSocketConnection(callback) {
      const component = this;
      const recursion = this.waitForSocketConnection;
      setTimeout(function () {
        if (WebSocketInstance.state() === 1) {
          console.log("Connection is secured");
          return;
        } else {
          console.log("Waiting for connection");
          waitForSocketConnection();
        }
      }, 100);
    }
  },
};
</script>