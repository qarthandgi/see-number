<?php

namespace App\Http\Controllers;

use App\User;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
require '../vendor/autoload.php';

class NumberController extends Controller
{
	public function __invoke(Request $request)
	{
		// error_log("hey1");
		// error_log(var_dump($request));
		$data_url = $request->dataUrl;
		$real_number = $request->realNumber;
		// error_log('between 1 and 2');
		// error_log($data_url);
		// error_log("hey2");
		$client = new \GuzzleHttp\Client();
		$res = $client->request('POST', '//service:5000/', [
			'form_params' => [
				'data_url' => $data_url,
				'real_number' => $real_number
			]
		]);
		// error_log("hey3");
		$py_response = $res->getBody();
		// error_log('************************OK');
		// error_log('Generic ok');
		return ($py_response);
	}
}