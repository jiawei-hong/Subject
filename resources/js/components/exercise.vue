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

        <div class="btn-flex">
            <button @click="prevIndex" class="btn btn-success w-50">上一題</button>
            <button @click="nextIndex" class="btn btn-success w-50">下一題</button>
        </div>

        <div class="card" v-if="data.questions">
            <div class="card-header text-center">
                <h2>
                    第 {{ currentIndex + 1 }} 題
                </h2>
            </div>

            <div class="card-body text-center xxs">
                <span class="topic">
                    {{ data.questions[currentIndex].content }}
                </span>

                <br>

                <div>
                    <ul>
                        <li v-for="(item,index) in data.options[currentIndex]">
                            <input :type="data.answer[currentIndex].length > 1 ? 'checkbox' : 'radio'"
                                   :name="currentIndex"
                                   :id="currentIndex"
                                   :value="item.id"
                                   :checked="questionsData[currentIndex] == item.id || Array.isArray(questionsData[currentIndex]) && [currentIndex].includes(item.id)"
                                   v-model="questionsData[currentIndex]"
                            >

                            <label :for="currentIndex">
                                {{ item.value }}
                            </label>
                        </li>
                    </ul>
                </div>
            </div>
        </div>

        <div>
            <button @click="judgeAnswers" class="btn btn-success w-100">結束作答</button>
        </div>
    </div>
</template>

<script>
    export default {
        data(){
            return {
                data:[],
                currentIndex:0,
                questionsData:[]
            }
        },
        mounted() {
            let categoryId = this.$route.params.id;

            api.getResult(categoryId).then(res => {
                this.data = res;
                this.currentIndex = 0;
                this.questionsData = new Array(this.data.questions.length).fill([]);
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
            },
            judgeAnswers(){
                let status = {
                    correct:0,
                    incorrect:0,
                    omitted:0
                };

                this.questionsData.forEach((item,index) => {
                    if(Array.isArray((item))){
                        if(item.length > 0){
                            let ans = item.map(ele => this.data.answer[index].includes(ele)).filter(ele => ele == true);

                            if(ans.length == item.length){
                                status.correct++;
                            }else{
                                status.incorrect++;
                            }
                        }else{
                            status.omitted++;
                        }
                    }else{
                        if(item == this.data.answer[index]){
                            status.correct++;
                        }else{
                            status.incorrect++;
                        }
                    }
                });

                swal.fire({
                    title:'結果',
                    text:`答對:${status.correct} \n 答錯:${status.incorrect} \n 未作答:${status.omitted}`,
                    icon:'question'
                });
            }
        }
    }
</script>
