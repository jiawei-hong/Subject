<template>
    <div class="container">
        <div class="card">
            <div class="card-header text-center">
                Subject Exercise
            </div>

            <div class="card-body">
                <div class="form-group">
                    <label for="cateogries">選擇題庫：</label>
                    <select class="form-control" v-model="categoriesId" id="cateogries">
                        <option v-for="item in categories" :value="item.id">
                            {{ item.name }}
                        </option>
                    </select>
                </div>

                <div class="form-group">
                    <label for="mode">選擇模式：</label>
                    <select class="form-control" v-model="mode" id="mode">
                        <option value="View" selected>查看</option>
                        <option value="Exercise">練習</option>
                    </select>
                </div>

                <router-link :to=" mode + '/' + categoriesId" class="btn btn-success btn-block">查看題目</router-link>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data(){
            return {
                mode:'View',
                categories:[],
                categoriesId:1
            }
        },
        mounted() {
            api.getCategories().then(res => {
                this.categories = res;
            });
        }
    }
</script>
