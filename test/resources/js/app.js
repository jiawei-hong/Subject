import router from './router';
import './prototype';

require('./bootstrap');

window.Vue = require('vue');

const app = new Vue({
    el: '#app',
    router
});
