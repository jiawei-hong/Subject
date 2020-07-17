<template>
    <div class="container">
        <div class="card text-center" v-for="(question,index) in data.questions">
            <div class="card-header">
                第 {{ index + 1 }} 題

                <br>

                {{ question.content }}
            </div>

            <div class="card-body">
                <button class="btn btn-block"  :class="data['answer'][index].includes(options['id']) ? 'btn-success' : 'btn-danger'" v-for="options in data.options[index]">{{ options.value }}</button>
            </div>
        </div>

        <router-link class="btn btn-success btn-block" to="/">查看完畢</router-link>
    </div>
</template>

<script>
    import api from '../api';

    export default {
        data(){
            return {
                data:[],
                maxPage:0,
                currentPage:1
            };
        },
        mounted() {
            let categoryId = this.$route.params.id;

            api.getQuestions(categoryId).then(res => {
                this.data = res;
                this.maxPage = this.data.questions.length / 5;

                console.log(res);
            });
        }
    }
</script>
