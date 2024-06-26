using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using AmirBlog.Data;
using AmirBlog.Models;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;

namespace AmirBlog.Controllers {
    public class PostController : Controller {
        private readonly ApplicationDbContext _context;
        private IHostingEnvironment _hostingEnvironment;

        public PostController (ApplicationDbContext context, IHostingEnvironment env) {
            _context = context;
            _hostingEnvironment = env;
        }

        // GET: Post
        public async Task<IActionResult> Index () {
            return View (await _context.Posts.OrderByDescending (d => d.Id).ToListAsync ());
        }

        public Task<string> Count (int id) {
            TaskCompletionSource<string> tcs = new TaskCompletionSource<string> ();
            Task.Run (() => {
                Post post = _context.Posts
                    .FirstOrDefault (m => m.Id == id);
                post.LoveCount += 1;
                _context.SaveChanges ();
            });
            return tcs.Task;
        }

        [HttpGet ("{Title}")]
        public async Task<IActionResult> Index (string Title) {
            Console.WriteLine ("\n\n" + Title + "\n\n");
            if (Title == "") {
                return View (await _context.Posts.OrderByDescending (d => d.Id).ToListAsync ());
            } else {
                return View (await _context.Posts.Where (a => a.Title.Contains (Title)).OrderByDescending (d => d.Id).ToListAsync ());
            }

        }

        public async Task<IActionResult> MyPosts () {
            return View (await _context.Posts.Where (a => a.Author == User.Identity.Name).OrderByDescending (d => d.Id).ToListAsync ());
        }

        // GET: Post/Details/5
        public async Task<IActionResult> Details (int? id) {
            if (id == null) {
                return NotFound ();
            }

            var post = await _context.Posts
                .FirstOrDefaultAsync (m => m.Id == id);
            if (post == null) {
                return NotFound ();
            }

            return View (post);
        }

        // GET: Post/Create
        public IActionResult Create () {
            if (User.Identity.IsAuthenticated) {
                return View ();
            } else {
                return Redirect ("/Identity/Account/Login");
            }
        }

        // POST: Post/Create
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        public async Task<IActionResult> Create ([Bind ("Id,Title,Text")] Post post, IFormFile file) {
            if (ModelState.IsValid) {
                var uploads = Path.Combine (_hostingEnvironment.WebRootPath, "uploads");
                if (file.Length > 0) {
                    using (var fileStream = new FileStream (Path.Combine (uploads, file.FileName), FileMode.Create)) {
                        await file.CopyToAsync (fileStream);
                    }
                }
                post.PublishedDate = DateTime.Now;
                post.Author = User.Identity.Name;
                post.Picture = Path.Combine ("https://localhost:5001/uploads/", file.FileName);
                _context.Add (post);
                await _context.SaveChangesAsync ();
                return RedirectToAction (nameof (Index));
            }
            return View (post);
        }

        // GET: Post/Edit/5
        public async Task<IActionResult> Edit (int? id) {
            if (id == null) {
                return NotFound ();
            }

            var post = await _context.Posts.FindAsync (id);
            if (post == null) {
                return NotFound ();
            }
            return View (post);
        }

        // POST: Post/Edit/5
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit (int id, [Bind ("Id,Title,Picture,Text,PublishedDate,Author,LoveCount")] Post post) {
            if (id != post.Id) {
                return NotFound ();
            }
            if (ModelState.IsValid) {
                try {
                    _context.Update (post);
                    await _context.SaveChangesAsync ();
                } catch (DbUpdateConcurrencyException) {
                    if (!PostExists (post.Id)) {
                        return NotFound ();
                    } else {
                        throw;
                    }
                }
                return RedirectToAction (nameof (Index));
            }
            return View (post);
        }

        // GET: Post/Delete/5
        public async Task<IActionResult> Delete (int? id) {
            if (id == null) {
                return NotFound ();
            }

            var post = await _context.Posts
                .FirstOrDefaultAsync (m => m.Id == id);
            if (post == null) {
                return NotFound ();
            }

            return View (post);
        }

        // POST: Post/Delete/5
        [HttpPost, ActionName ("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed (int id) {
            var post = await _context.Posts.FindAsync (id);
            _context.Posts.Remove (post);
            await _context.SaveChangesAsync ();
            return RedirectToAction (nameof (Index));
        }

        private bool PostExists (int id) {
            return _context.Posts.Any (e => e.Id == id);
        }
    }
}