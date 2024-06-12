using System;

namespace AmirBlog.Models {
    public class Post {
        public int Id { get; set; }
        public string Picture { get; set; }
        public string Title { get; set; }
        public string Text { get; set; }
        public DateTime PublishedDate { get; set; }
        public string Author { get; set; }
        public int LoveCount { get; set; } = 0;
    }
}