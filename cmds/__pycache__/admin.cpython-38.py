U
    �7`�  �                   @   sb   d dl Z d dlmZ d dlZd dlZd dlZd dlZd dlZd dlZG dd� dej	�Z
dd� ZdS )�    N)�commandsc                   @   s�   e Zd Zdd� Ze�� ejdd�dd� ��Ze�� ejdd�dd� ��Ze�� ejdd�dd	d
�e	j
d�dd���Ze�� ejdd�dd	d
�e	j
d�dd���Zd	S )�Adminc                 C   s
   || _ d S �N��bot)�selfr   � r   �/home/runner/ROC/cmds/admin.py�__init__   s    zAdmin.__init__T)�administratorc                �   sL   |j �� I d H  tjdt�dd�d�}|jd|d� |jd|d�I d H  d S )	Nu   公告r   ���� )�title�coloru   訊息)�name�valuez||@everyone||��embed)�message�delete�discord�Embed�random�randint�	add_field�send)r   �ctx�msgr   r   r   r	   �anno   s    z
Admin.annoc                 �   s^   g }| j jD ]*}|j� d|j� d|j� d�}|�|� qd�|�}|�d|� d��I d H  d S )N�(�[z])z

z```)r   �guildsr   �id�owner�append�joinr   )r   r   Z	guildlist�listZnameid�guildr   r   r	   r&      s    
zAdmin.guildN��reason)�memberc                �   s  t jddt�dd�d�}t jddt�dd�d�}|d krL|j|d�I d H  n�||jkrl|j|d�I d H  d S t jdd	tj�� d
�}|j||j	d� |j
d|� dd� |j
d|jj� d|jj� �dd� |jdd� |j|d�I d H  |j|d�I d H  | j�|j�}|j|d�I d H  d S )N�   **指令錯誤**u   你不能踢出你自己r   r   �r   �description�colouru;   請輸入一位成員
**用法**
c!kick @Member/ID <reason>r   u   踢出�}�� �r   r   �	timestamp�r   �icon_url�   原因F�r   r   �inline�	   執行者�#�/   kuan 🇹🇼#6503|coal|XiaYue#0898技術支援��textr'   )r   r   r   r   r   �author�datetime�utcnow�
set_author�
avatar_urlr   r   �discriminator�
set_footer�kickr   �get_userr!   )r   r   r)   r(   r   Zembed2�embedTW3�userr   r   r	   rB       s     
"z
Admin.kickc                �   s  t jddt�dd�d�}t jddt�dd�d�}|d krN|j|d�I d H  d S ||jkrn|j|d�I d H  d S t jdd	tj�� d
�}|j||j	d� |j
d|� dd� |jdd� |j
d|jj� d|jj� �dd� |j|d�I d H  |j|d�I d H  | j�|j�}|j|d�I d H  d S )Nr*   u   你不能封鎖你自己r   r   r+   u:   請輸入一位成員
**用法**
c!ban @Member/ID <reason>r   u   封鎖r.   r/   r1   r3   Fr4   r8   r9   r6   r7   r'   )r   r   r   r   r   r;   r<   r=   r>   r?   r   rA   r   r@   �banr   rC   r!   )r   r   r)   r(   ZembedTW1ZembedTW4rD   rE   r   r   r	   rF   5   s"    
"z	Admin.ban)N)N)�__name__�
__module__�__qualname__r
   r   �command�has_permissionsr   r&   r   �MemberrB   rF   r   r   r   r	   r   
   s   



r   c                 C   s   | � t| �� d S r   )�add_cogr   r   r   r   r	   �setupP   s    rN   )r   �discord.extr   �json�asyncior<   �timer   �os�Cogr   rN   r   r   r   r	   �<module>   s   F