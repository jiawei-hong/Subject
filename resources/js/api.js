import axios from 'axios';

export default {
    getCategories: function () {
        return axios.get('/api/category').then(res => {
            if(res.status){
                return res.data;
            }
        });
    },
    getQuestions: function(id,data){
        return axios.get(`/api/category/${id}`,data).then(res => {
            if(res.status){
                return res.data;
            }
        });
    }
};
