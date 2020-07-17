import VueRouter from 'vue-router';

let routes = [
    {
        path:'/',
        component:require('./components/home').default
    },
    {
        path:'/view/:id',
        component: require('./components/viewQuestion').default
    },
    {
        path:'/exercise/:id',
        component: require('./components/exercise').default
    },
    {
        path:'*',
        component: require('./components/pageNotFound').default
    }
];

export  default  new VueRouter({
    mode:'history',
    routes
});
