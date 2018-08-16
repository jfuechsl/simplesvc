# simplesvc
A very simple service for testing purposes.

The service listens on port 5000 and on the root (`/`) route exposes an html page with:
  * A list of volume mounts. This can be used to test if Docker volumes are actually there.
  * A list of environment variables (starting with `EY_`).
  * Some content (the current [xkcd](https://xkcd.com/) comic) pulled from an API.
