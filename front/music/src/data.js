import { v4 as uuidv4 } from "uuid";

import { BASE_URL } from "./config/baseurl.js";
import axios from "axios";
import { useEffect,useState } from 'react';
function ChillHop() {


    const [datas, setData] = useState({data: []})
	const API = `${BASE_URL}/music/`;
	const fetchPost = () => {
	  fetch(API)
		.then((res) => res.json())
		.then((res) => {
		  console.log(res)
		  setData(res)
		})
	}
	useEffect(() => {
	  fetchPost()
	}, [])
	return [fetchPost()]
// 	useEffect(() =>{
// 		axios.get(
// 			`${BASE_URL}/music/`,).then(response => {
// 			console.log(response.data)
// 			setData(response.data);
// 			// console.log(data); // log the data to check if it's being fetched correctly
// 		  }).catch(error => {
// 			console.error(error)
// 		  });
// }, [])

// useEffect(() => {
// 	fetch(`${BASE_URL}/music/`)
// 	  .then((response) => {
// 		if (!response.ok) {
// 		  throw new Error(
// 			`This is an HTTP error: The status is ${response.status}`
// 		  );
// 		}
// 		return response.data;
// 	  })
// 	  .then((actualData) => (setData(actualData) ))
// 	  .catch((err) => {
// 		console.log(err.message);
// 	  });
//   }, []);

		// return [
		// 	{
		// 		name: "student",
		// 		cover: "http://localhost:8000/media/images/12255-2021-kia-k5.png",
		// 		artist: {
		// 			psevdo_name: "Polna"
		// 		},
		// 		audio: "http://localhost:8000/media/music/10075.mp3",
		// 		// color: ["#205950", "#2ab3bf"],
		// 		id: 1,
		// 		active: true
		// 	},
		// 	{
		// 		name: "student",
		// 		cover: "http://localhost:8000/media/images/12255-2021-kia-k5.png",
		// 		artist: {
		// 			psevdo_name: "Polna"
		// 		},
		// 		audio: "http://localhost:8000/media/music/10075.mp3",
		// 		// color: ["#205950", "#2ab3bf"],
		// 		id: 2,
		// 		active: false
		// 	},
		// 	];

		}

		export default ChillHop;







		// 	name: "test 2",
		// 	cover: "http://localhost:8000/media/images/zyro-image.png",
		// 	artist: {
		// 		psevdo_name: "Polna2"
		// 	},
		// 	audio: "http://localhost:8000/media/music/%D0%94%D0%BE%D1%81-%D0%9C%D2%B1%D2%9B%D0%B0%D1%81%D0%B0%D0%BD_-_%D0%A2%D0%BE%D0%B9_%D0%B6%D1%8B%D1%80%D1%8B.mp3",
		// 	// color: ["#205950", "#2ab3bf"],
		// 	id: 2,
		// 	active: false
		// },
		// {   
// 			name: "Твои глаза",
// 			cover: "http://localhost:8000/media/images/47e82181-0805-440e-bd73-0cf403e833a1.jpeg",
// 			artist: {
// 				psevdo_name: "Polna3"
// 			},
// 			audio: "http://localhost:8000/media/music/Polnalyubvi_-_%D0%A2%D0%B2%D0%BE%D0%B8_%D0%B3%D0%BB%D0%B0%D0%B7%D0%B0.mp3",
// 			// color: ["#205950", "#2ab3bf"],
// 			id: 3,
// 			active: false

//     }
// ];
	// return [
	// 	{
	// 		name: "Beaver Creek",
	// 		cover:
	// 			"https://chillhop.com/wp-content/uploads/2020/09/0255e8b8c74c90d4a27c594b3452b2daafae608d-1024x1024.jpg",
	// 		artist: "Aso, Middle School, Aviino",
	// 		audio: "https://mp3.chillhop.com/serve.php/?mp3=10075",
	// 		color: ["#205950", "#2ab3bf"],
	// 		id: uuidv4(),
	// 		active: true,
	// 	},
	// 	{
	// 		name: "Daylight",
	// 		cover:
	// 			"https://chillhop.com/wp-content/uploads/2020/07/ef95e219a44869318b7806e9f0f794a1f9c451e4-1024x1024.jpg",
	// 		artist: "Aiguille",
	// 		audio: "https://mp3.chillhop.com/serve.php/?mp3=9272",
	// 		color: ["#EF8EA9", "#ab417f"],
	// 		id: uuidv4(),
	// 		active: false,
	// 	},
	// 	{
	// 		name: "Keep Going",
	// 		cover:
	// 			"https://chillhop.com/wp-content/uploads/2020/07/ff35dede32321a8aa0953809812941bcf8a6bd35-1024x1024.jpg",
	// 		artist: "Swørn",
	// 		audio: "https://mp3.chillhop.com/serve.php/?mp3=9222",
	// 		color: ["#CD607D", "#c94043"],
	// 		id: uuidv4(),
	// 		active: false,
	// 	},
	// 	{
	// 		name: "Nightfall",
	// 		cover:
	// 			"https://chillhop.com/wp-content/uploads/2020/07/ef95e219a44869318b7806e9f0f794a1f9c451e4-1024x1024.jpg",
	// 		artist: "Aiguille",
	// 		audio: "https://mp3.chillhop.com/serve.php/?mp3=9148",
	// 		color: ["#EF8EA9", "#ab417f"],
	// 		id: uuidv4(),
	// 		active: false,
	// 	},
	// 	{
	// 		name: "Reflection",
	// 		cover:
	// 			"https://chillhop.com/wp-content/uploads/2020/07/ff35dede32321a8aa0953809812941bcf8a6bd35-1024x1024.jpg",
	// 		artist: "Swørn",
	// 		audio: "https://mp3.chillhop.com/serve.php/?mp3=9228",
	// 		color: ["#CD607D", "#c94043"],
	// 		id: uuidv4(),
	// 		active: false,
	// 	},
	// 	{
	// 		name: "Under the City Stars",
	// 		cover:
	// 			"https://chillhop.com/wp-content/uploads/2020/09/0255e8b8c74c90d4a27c594b3452b2daafae608d-1024x1024.jpg",
	// 		artist: "Aso, Middle School, Aviino",
	// 		audio: "https://mp3.chillhop.com/serve.php/?mp3=10074",
	// 		color: ["#205950", "#2ab3bf"],
	// 		id: uuidv4(),
	// 		active: false,
	// 	},
	// 	//ADD MORE HERE
	// ];
