import logging
import os
import yagooglesearch


class scrapper:

    @staticmethod
    def scrap_google(**kwargs):
        query = kwargs.get("query") or ""
        max_res = kwargs.get("max")
        max_res = max_res if isinstance(max_res, int) and max_res > 0 else 100
        country = kwargs.get("country") or ""
        tbs = kwargs.get("tbs") or ""
        proxy = kwargs.get("proxy") or ""
        logger = kwargs.get("logger")
        
        if proxy:
            logger.info(f"using proxy: {proxy}")
    
        if country:
            logger.info(f"looking in {country}")
            
        logger.info(f"using query: {query}")
        logger.info(f"result limits: {max_res}")

        client = yagooglesearch.SearchClient(
            query=query,
            max_search_result_urls_to_return=max_res,
            proxy=proxy,
            country=country,
            verify_ssl=(not proxy.startswith("http:")),
            tbs=tbs,
            verbosity=0,
            http_429_cool_off_time_in_minutes=5
        )

        client.search()

        return client.search_result_list


class Plugin:
    def __init__(self, utils=None, **kwargs):
        self.kwargs = kwargs
        self.utils = utils
        self.logger = logging.getLogger(os.getenv("root_logger_name") or __file__)
        self.logger.info(f"initializing SearchByName ...")

    def __repr__(self):
        return "<BuiltinPlugin@SearchByName>"

    def make_google_search(self) -> str | None:
        name = self.kwargs.get("name") or self.kwargs.get("username")

        if not isinstance(name, str):
            return None

        query = f'"{name}"' if (self.kwargs.get("google") or {}).get("exact") else name
        query += " " + f"intext:{name}" + " " + f"intitle:{name}" + " " + f"inurl:{name}"

        return query

    def start(self) -> list | dict:
        """
        Params
        ======
        name: dict
        exact: bool
        max: int
        country: str
        tbs: str
        """

        # initializing a parser
        search_query = self.make_google_search()

        if not search_query:
            self.logger.critical("no name was provided!")
            return []

        proxy = self.utils.config.read("proxy/http")
        results = []
        kw = self.kwargs.get("google") or {}
        google_results = scrapper.scrap_google(proxy=proxy, query=search_query, logger=self.logger, **kw)

        results.append(google_results)

        return []


# Useless as your LinkedIn profile
class Parser:
    pass
