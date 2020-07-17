<?php

use Illuminate\Database\Seeder;
use App\Category;
use App\Question;
use App\Option;
use App\Answer;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     *
     * @return void
     */
    public function run()
    {
        $dataset = [
            '網頁設計 乙級' => '173002A12.txt',
        ];

        foreach($dataset as $category => $fn){
            $categoryData = Category::create([
                'name' => $category
            ]);

            $raw_data = file_get_contents(__DIR__ . "/../data/{$fn}");
            $raw_data = array_filter(array_map(function($d){
                return preg_replace('/\s(?=)/u','',$d);
            },explode('。',$raw_data)),function($d){
                return $d !== '';
            });

            foreach($raw_data as $key => $item){
                preg_match_all('/\(([0-9]+).([^①]+).([^②]+).([^③]+).([^④]+).(.*)/u',$item,$output);

                $questionData = Question::create([
                    'content' => $output[2][0],
                    'category_id' => $categoryData->id
                ]);

                $options = [
                    Option::create(['question_id' => $questionData->id,'value' => $output[3][0]]),
                    Option::create(['question_id' => $questionData->id,'value' => $output[4][0]]),
                    Option::create(['question_id' => $questionData->id,'value' => $output[5][0]]),
                    Option::create(['question_id' => $questionData->id,'value' => $output[6][0]]),
                ];

                foreach(str_split($output[1][0]) as $optionId){
                    Answer::create([
                        'question_id' => $questionData->id,
                        'option_id' => $options[$optionId - 1]->id
                    ]);
                }
            }
        }
    }
}
