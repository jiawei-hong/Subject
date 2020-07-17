<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Category;
use App\Question;
use App\Option;
use App\Answer;
use League\Flysystem\Adapter\AbstractAdapter;

class ApiController extends Controller
{
    public function getCategories()
    {
        return Category::get();
    }

//    public function getQuestions(Request $req)
//    {
//        $data = [
//            'questions' => Question::where('category_id',$req->id)->inRandomOrder()->take(30)->get(),
//            'answer' => [],
//            'options' => []
//        ];
//
//        foreach($data['questions'] as $key => $question){
//            array_push($data['options'],$this->getOptions($question->id));
//            array_push($data['answer'],$this->getAnswer($question->id));
//        };
//    }

    public function getQuestions(Request $req){
        return Question::where('category_id',$req->id)->inRandomOrder()->take(30)->get();
    }

    public function getOptions($questionId){
        return Option::where('question_id',$questionId)->get();
    }

    public function getAnswer($questionId){
        return collect(Answer::select('option_id')->where('question_id',$questionId)->get())->pluck('option_id')->all();
    }
}
