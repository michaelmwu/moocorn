const API_URL = import.meta.env.VITE_MOOCORN_API_URL || 'http://localhost:8888';

export const generatePopcorn = async (name: string, mood: string, image: File | null) => {
  const formData = new FormData();
  formData.append('name', name);
  formData.append('mood', mood);
  if (image) {
    formData.append('image', image);
  }

  const response = await fetch(`${API_URL}/generate_popcorn`, {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    throw new Error('Failed to generate popcorn');
  }

  return response.json();
};
