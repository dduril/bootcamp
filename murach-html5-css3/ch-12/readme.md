## HTML5 and CSS3

### Audio and Video

**About these pages:** *Notes and code samples from **[Murach's HTML5 and CSS3, 3rd Edition](https://www.murach.com/shop/murachs-html5-and-css3-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

**Object element**

    <object type="audio/mpeg"
            data="media/[file_name].mp3"
            width="400" height="25">
        <param name="volume" value="100">
        <param name="autoplay" value="true">
    </object>

    <object type="application/x-shockwave-flash"
            data="media/[file_name].swf"
            width="400" height="100">
        <param name="autoplay" value="true">
    </object>

**Embed element**

    <embed type="audio/mp3" 
	   src="media/[file_name].mp3"
       width="400" height="50"
       autoplay="true">

    <embed src="https://www.youtube.com/embed/[file_name]"
           width="600"
           height="350">

**Video element**

    <video id="videoplayer" width="480" height="270" controls autoplay>
	<source src="media/[file_name].mp4">
	
	<!--<source src="media/[file_name].webm" 
	        type='video/webm; codecs="vp8, vorbis"'>-->
			
	<!--<source src="media/[file_name].ogv" 
            type='video/ogg; codecs="theora, vorbis"'>-->

    </video>

**Audio element**

    <audio id="audioplayer" controls autoplay>
    <source src="media/[file_name].mp3">
	<!--<source src="media/[file_name].ogg">-->
    </audio>