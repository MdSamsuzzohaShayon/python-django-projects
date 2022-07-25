import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import SuiVue from 'semantic-ui-vue';
import 'semantic-ui-css/semantic.min.css';

const app = createApp(App);

app.use(router);
app.use(SuiVue);

app.mount('#app');




