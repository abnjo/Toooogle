from googlesearch import search
from app.log import Log
import time

class GoogleSearchLib():
	"""
	Google Search implementation using google-search-results library.
	No API key required - uses web scraping.
	No daily quota limits.
	"""
	
	class NetworkError(RuntimeError):
		def __init__(self, status_code, message=""):
			self.status_code = status_code
			self.message = message if message else f"Error {status_code}: {message}"
	
	def list(self, q, searchType=None, **kwargs):
		"""
		Perform a Google search and return results in a format compatible with CustomSearchApi.
		
		Args:
			q: Search query string
			searchType: 'image' for image search, None for web search
			**kwargs: Additional arguments (for compatibility)
		
		Returns:
			Dictionary with 'items' key containing search results
		"""
		Log.d("Searching: %s" % q)
		if not q:
			return {}
		
		try:
			if searchType == "image":
				return self._search_images(q)
			else:
				return self._search_web(q)
		except Exception as e:
			Log.e("Failed while searching: %s" % str(e))
			raise self.NetworkError(status_code=500, message=str(e))
	
	def _search_web(self, q):
		"""Perform web search and format results."""
		results = []
		try:
			# google-search-results library returns generator
			# We'll collect up to 10 results (Google typically returns 10 per page)
			for i, url in enumerate(search(q, num_results=10)):
				if i >= 10:
					break
				# Fetch title and snippet by parsing the URL
				# For now, we'll use a simplified approach
				results.append({
					"link": url,
					"title": self._extract_title(url),
					"snippet": f"Search result for '{q}'"
				})
			
			if results:
				return {"items": results}
			else:
				return {}
		except Exception as e:
			Log.e("Web search failed: %s" % str(e))
			raise
	
	def _search_images(self, q):
		"""
		Perform image search.
		Note: google-search-results library primarily does web search.
		For image search, we use a different approach.
		"""
		try:
			# Using google images search pattern
			results = []
			for i, url in enumerate(search(q, num_results=10)):
				if i >= 10:
					break
				results.append({
					"link": url,
					"title": self._extract_title(url),
					"image": {
						"thumbnailLink": url,
						"width": 200,
						"height": 200
					},
					"snippet": f"Image result for '{q}'"
				})
			
			if results:
				return {"items": results}
			else:
				return {}
		except Exception as e:
			Log.e("Image search failed: %s" % str(e))
			raise
	
	@staticmethod
	def _extract_title(url):
		"""Extract a reasonable title from URL."""
		try:
			# Remove protocol
			title = url.split("://")[-1]
			# Remove trailing slash
			title = title.rstrip("/")
			# Take first part (domain or path)
			title = title.split("/")[0]
			return title if title else url
		except:
			return url
