from abc import ABC, abstractmethod
from typing import List
from app.entities.processed_agent_data import ProcessedAgentData
import requests
import logging


class StoreGateway(ABC):
    """
    Abstract class representing the Store Gateway interface.
    All store gateway adapters must implement these methods.
    """

    @abstractmethod
    def save_data(self, processed_agent_data_batch: List[ProcessedAgentData]) -> bool:
        try:
            response = requests.post(
                f"{self.api_base_url}/processed_agent_data/batch",
                json=[data.model_dump() for data in processed_agent_data_batch],
                timeout=10,
            )
            response.raise_for_status()
            logging.info(f"Successfully saved {len(processed_agent_data_batch)} entries to Store API.")
            return True
        except requests.RequestException as e:
            logging.error(f"Failed to save data to Store API: {e}")
            return False

        pass
