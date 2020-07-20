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
                題目
            </div>

            <div class="card-body text-center">
                <h2>
                    {{ data.questions[currentIndex].content }}
                </h2>

                <br>

                <div>
                    <ul>
                        <li v-for="(item,index) in data.options[currentIndex]">
                            <input :type="data.answer[currentIndex].length > 1 ? 'checkbox' : 'radio'" :id="currentIndex" :value="item.value">

                            <label :for="currentIndex">
                                {{ item.value }}
                            </label>
                        </li>
                    </ul>
                </div>
            </div>
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
                this.questionsData = new Array(this.data.quesitions.length);

                console.log(this.questionsData)
            });
        },
        methods:{
            changeCurrentIndex(index){
                this.currentIndex = index;
            }
        }
    }
</script>
