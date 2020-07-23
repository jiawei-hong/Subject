<template>
    <div class="container">
        <div class="card">
            <div class="card-header text-center">
                Subject Exercise
            </div>

            <div class="card-body">
                <div class="form-group">
                    <button @click="changeCurrentIndex(index)" class="btn btn-dark" v-for="(item,index) in data.questions">
                        {{ index + 1 }}
                    </button>
                </div>
            </div>
        </div>

        <div class="card" v-if="data.questions">
            <div class="card-header text-center">
                <h2>
                    第 {{ currentIndex + 1 }} 題
                </h2>
            </div>

            <div class="card-body text-center">
                <span class="topic">
                    {{ data.questions[currentIndex].content }}
                </span>

                <br>

                <div v-if="data.questions">
                    <ul>
                        <li v-for="(item,index) in data.options[currentIndex]">
                            <button class="btn btn-block btn-lg" :class="data['answer'][currentIndex].includes(item.id) ? 'btn-success' : 'btn-danger'">{{ item.value }}</button>
                        </li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="btn-flex">
            <button @click="prevIndex" class="btn btn-success w-50">上一題</button>
            <button @click="nextIndex" class="btn btn-success w-50">下一題</button>
        </div>
    </div>
</template>

<script>
    export default {
        data(){
            return {
                data:[],
                currentIndex:0
            }
        },
        mounted() {
            let categoryId = this.$route.params.id;

            api.getResult(categoryId).then(res => {
                this.data = res;
                this.currentIndex = 0;
                this.questionsData = new Array(this.data.questions.length);
            });
        },
        methods:{
            changeCurrentIndex(index){
                this.currentIndex = index;
            },
            prevIndex(){
                if(this.currentIndex == 0){
                    this.currentIndex = this.data.questions.length - 1;
                }else{
                    this.currentIndex--;
                }
            },
            nextIndex(){
                if(this.currentIndex >= this.data.questions.length - 1){
                    this.currentIndex = 0;
                }else{
                    this.currentIndex++;
                }
            }
        }
    }
</script>

