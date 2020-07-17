Object.defineProperties(Array.prototype,{
    first:{
        get:function(){
            return this[0];
        }
    },
    last:{
        get:function(){
            return this[this.length - 1];
        }
    }
})
