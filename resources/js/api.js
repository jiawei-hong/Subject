import axios from 'axios';

export default {
    getCategories: function () {
        return axios.get('/api/category').then(res => {
            if(res.status){
                return res.data;
            }
        });
    },
    getResult: function(id){
        return axios.get(`/api/category/${id}`).then(res => {
            if(res.status){
                return res.data;
            }
        });
    }
};
