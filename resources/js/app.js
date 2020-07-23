import router from './router';
import api from './api';

require('./bootstrap');

window.Vue = require('vue');
window.api = api;
window.swal = require('sweetalert2');

const app = new Vue({
    el: '#app',
    router
});
